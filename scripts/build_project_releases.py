#!/usr/bin/env python3
from __future__ import annotations

import gzip
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

R = Path(__file__).resolve().parents[1]
K = R / 'src/kb'
P = R / 'src/project'
V = 'v1.3.1'
D = R / 'releases' / V
FIXED = (2026, 9, 11, 12, 0, 0)

PLATFORMS = {
    'chatgpt': ('CHATGPT_INSTRUCTIONS.md', 'CharlyNé — Projet ChatGPT'),
    'claude': ('CLAUDE.md', 'CharlyNé — Projet Claude'),
    'gemini': ('GEMINI_INSTRUCTIONS.md', 'CharlyNé — Gem Gemini'),
}

KB_FILES = [
    'charly_competences.jsonl',
    'charly_kb_manifest.json',
    'charly_relations.jsonl',
    'charly_schema.json',
    'charly_sources.jsonl',
]


def package_readme(platform: str, title: str) -> str:
    if platform == 'chatgpt':
        steps = (
            '1. Décompresser cette archive sur un ordinateur.\n'
            '2. Dans ChatGPT, créer un nouveau Projet.\n'
            '3. Copier le contenu de `INSTRUCTIONS.md` dans les instructions du Projet.\n'
            '4. Ajouter les six fichiers du dossier `kb/` aux fichiers du Projet.\n'
            '5. Ouvrir une nouvelle conversation dans le Projet et poser directement une question à CharlyNé.\n'
        )
    elif platform == 'claude':
        steps = (
            '1. Décompresser cette archive sur un ordinateur.\n'
            '2. Dans Claude, créer un nouveau Projet.\n'
            '3. Copier le contenu de `INSTRUCTIONS.md` dans les instructions du Projet.\n'
            '4. Ajouter les six fichiers du dossier `kb/` à la connaissance du Projet.\n'
            '5. Ouvrir une nouvelle conversation dans le Projet et poser directement une question à CharlyNé.\n'
        )
    else:
        steps = (
            '1. Décompresser cette archive sur un ordinateur.\n'
            '2. Dans Gemini, créer un nouveau Gem.\n'
            '3. Copier le contenu de `INSTRUCTIONS.md` dans les instructions du Gem.\n'
            '4. Ajouter les six fichiers du dossier `kb/` comme fichiers de connaissance lorsque cette option est disponible.\n'
            '5. Démarrer une conversation avec le Gem et poser directement une question à CharlyNé.\n'
        )
    return f'''# {title}\n\nPackage Projet CharlyNé — release de distribution {V}.\n\nLa base de connaissance est identique dans les packages ChatGPT, Claude et Gemini. Seules les instructions d’adaptation à la plateforme diffèrent.\n\n## Installation\n\n{steps}\n## Utilisation\n\nHandle principal : `@charly`.\n\nAlias reconnus : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`.\n\n## Contenu\n\n- `INSTRUCTIONS.md` : socle Charly + adaptateur plateforme fusionnés ;\n- `kb/charly_knowledge.jsonl` : connaissances actives ;\n- `kb/charly_competences.jsonl` : catalogue de compétences ;\n- `kb/charly_relations.jsonl` : relations ;\n- `kb/charly_sources.jsonl` : sources ;\n- `kb/charly_schema.json` : schéma runtime ;\n- `kb/charly_kb_manifest.json` : manifeste de KB.\n\nAuteur : Maximatique - Bureau NÉ 13 -  Aix en Provence\n'''


def write_zip(root: Path, out: Path) -> dict:
    files = sorted(p for p in root.rglob('*') if p.is_file())
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            name = str(PurePosixPath(root.name) / p.relative_to(root).as_posix())
            info = zipfile.ZipInfo(name, FIXED)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes())
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        if bad:
            raise SystemExit(f'zip validation failed: {bad}')
    data = out.read_bytes()
    return {'file': out.name, 'size_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'entries': len(files)}


def main():
    required = [P / 'COMMON_INSTRUCTIONS.md', K / 'charly_knowledge.jsonl.gz']
    required += [P / x[0] for x in PLATFORMS.values()]
    required += [K / x for x in KB_FILES]
    for p in required:
        if not p.is_file():
            raise SystemExit(f'missing {p.relative_to(R)}')

    manifest = json.loads((K / 'charly_kb_manifest.json').read_text(encoding='utf-8'))
    if manifest.get('release_version') != '1.3.0' or manifest.get('runtime_active') != 113:
        raise SystemExit('unexpected KB manifest version/count')

    with gzip.open(K / 'charly_knowledge.jsonl.gz', 'rt', encoding='utf-8') as f:
        knowledge = f.read()
    if len([x for x in knowledge.splitlines() if x.strip()]) != 113:
        raise SystemExit('knowledge count mismatch')

    common = (P / 'COMMON_INSTRUCTIONS.md').read_text(encoding='utf-8').rstrip() + '\n\n'
    D.mkdir(parents=True, exist_ok=True)
    results = []

    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        for platform, (adapter_name, title) in PLATFORMS.items():
            root = temp / f'charly-{platform}-project'
            kb = root / 'kb'
            kb.mkdir(parents=True)
            adapter = (P / adapter_name).read_text(encoding='utf-8').strip()
            (root / 'INSTRUCTIONS.md').write_text(common + adapter + '\n', encoding='utf-8')
            (root / 'README.md').write_text(package_readme(platform, title), encoding='utf-8')
            for name in KB_FILES:
                shutil.copy2(K / name, kb / name)
            (kb / 'charly_knowledge.jsonl').write_text(knowledge, encoding='utf-8')
            out = D / f'charly-{platform}-project.zip'
            results.append({'platform': platform, **write_zip(root, out)})

    skill_src = R / 'skill.zip'
    if skill_src.is_file():
        shutil.copyfile(skill_src, D / 'skill.zip')
        data = (D / 'skill.zip').read_bytes()
        results.append({'platform': 'skill', 'file': 'skill.zip', 'size_bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'entries': 11})

    kb_hashes = {}
    for name in KB_FILES:
        kb_hashes[name] = hashlib.sha256((K / name).read_bytes()).hexdigest()
    kb_hashes['charly_knowledge.jsonl'] = hashlib.sha256(knowledge.encode('utf-8')).hexdigest()

    report = {
        'release': V,
        'status': 'PASS',
        'distribution_change': 'platform-specific project packages added',
        'kb_logical_version': manifest.get('release_version'),
        'ontology_version': manifest.get('ontology_version'),
        'knowledge_runtime': 113,
        'packages': results,
        'shared_kb_hashes': kb_hashes,
        'same_kb_across_project_packages': True,
        'skill_runtime_changed': False,
        'legal_review_required': True,
        'validated_at': '2026-09-11',
    }
    (D / 'project-validation-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
