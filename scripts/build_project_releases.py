#!/usr/bin/env python3
from __future__ import annotations
import gzip, hashlib, json, shutil, tempfile, zipfile
from pathlib import Path, PurePosixPath

R=Path(__file__).resolve().parents[1]; K=R/'src/kb'; P=R/'src/project'; V='v1.4.0'; D=R/'releases'/V
FIXED=(2026,9,12,12,0,0)
PLATFORMS={'chatgpt':('CHATGPT_INSTRUCTIONS.md','CharlyNé — Projet ChatGPT'),'claude':('CLAUDE.md','CharlyNé — Projet Claude'),'gemini':('GEMINI_INSTRUCTIONS.md','CharlyNé — Gem Gemini'),'universal':(None,'CharlyNé — Universal Markdown')}
KB_FILES=['charly_competences.jsonl','charly_kb_manifest.json','charly_relations.jsonl','charly_schema.json','charly_sources.jsonl']

def package_readme(platform,title):
    target={'chatgpt':'un Projet ChatGPT','claude':'un Projet Claude','gemini':'un Gem Gemini','universal':'un assistant/projet compatible Markdown'}[platform]
    return f'''# {title}\n\nPackage CharlyNé — release {V}.\n\nLa KB Core est identique dans tous les packages. La couche KB Live est référencée par le manifeste et n'est consultée que lorsque la plateforme dispose d'un accès web/Drive compatible.\n\n## Installation\n\n1. Décompresser cette archive sur un ordinateur.\n2. Créer {target}.\n3. Copier `INSTRUCTIONS.md` dans les instructions.\n4. Ajouter les six fichiers du dossier `kb/` comme fichiers de connaissance.\n5. Commencer à utiliser CharlyNé.\n\n## Utilisation\n\nHandle principal : `@charly`.\nAlias : `@charlyné`, `CoachNé`, `Lisnardassistant`, `assitantné`, `Charlyne`, `coachmilitant`.\n\nAuteur : Maximatique - Bureau NÉ 13 -  Aix en Provence\n'''

def write_zip(root,out):
    files=sorted(p for p in root.rglob('*') if p.is_file())
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for path in files:
            name=str(PurePosixPath(root.name)/path.relative_to(root).as_posix()); info=zipfile.ZipInfo(name,FIXED); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16; z.writestr(info,path.read_bytes())
    with zipfile.ZipFile(out) as z:
        if z.testzip(): raise SystemExit(f'zip validation failed: {out}')
    data=out.read_bytes(); return {'file':out.name,'size_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'entries':len(files)}

def main():
    required=[P/'COMMON_INSTRUCTIONS.md',K/'charly_knowledge.jsonl.gz']+[K/x for x in KB_FILES]+[P/x[0] for x in PLATFORMS.values() if x[0]]
    for path in required:
        if not path.is_file(): raise SystemExit(f'missing {path.relative_to(R)}')
    manifest=json.loads((K/'charly_kb_manifest.json').read_text(encoding='utf-8'))
    if manifest.get('release_version')!='1.4.0' or manifest.get('runtime_active')!=115: raise SystemExit('unexpected manifest')
    with gzip.open(K/'charly_knowledge.jsonl.gz','rt',encoding='utf-8') as f: knowledge=f.read()
    if len([x for x in knowledge.splitlines() if x.strip()])!=115: raise SystemExit('knowledge count mismatch')
    common=(P/'COMMON_INSTRUCTIONS.md').read_text(encoding='utf-8').rstrip()+'\n\n'; D.mkdir(parents=True,exist_ok=True); results=[]
    with tempfile.TemporaryDirectory() as td:
        temp=Path(td)
        for platform,(adapter_name,title) in PLATFORMS.items():
            root=temp/f'charly-{platform}-project'; kb=root/'kb'; kb.mkdir(parents=True)
            adapter=(P/adapter_name).read_text(encoding='utf-8').strip() if adapter_name else '# Adaptateur Universal Markdown\n\nAppliquer le socle commun sans dépendance spécifique à une plateforme.'
            (root/'INSTRUCTIONS.md').write_text(common+adapter+'\n',encoding='utf-8'); (root/'README.md').write_text(package_readme(platform,title),encoding='utf-8')
            for name in KB_FILES: shutil.copy2(K/name,kb/name)
            (kb/'charly_knowledge.jsonl').write_text(knowledge,encoding='utf-8')
            results.append({'platform':platform,**write_zip(root,D/f'charly-{platform}-project.zip')})
    skill_src=R/'skill.zip'
    if not skill_src.is_file(): raise SystemExit('skill.zip missing; run build_skill_release.py first')
    shutil.copyfile(skill_src,D/'skill.zip'); data=(D/'skill.zip').read_bytes(); results.append({'platform':'skill','file':'skill.zip','size_bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'entries':11})
    hashes={name:hashlib.sha256((K/name).read_bytes()).hexdigest() for name in KB_FILES}; hashes['charly_knowledge.jsonl']=hashlib.sha256(knowledge.encode('utf-8')).hexdigest()
    report={'release':V,'status':'PASS','distribution_change':'KB Core 0.4.0 + optional KB Live refresh','spec_version':'1.3','ontology_version':'0.4.0','knowledge_runtime':115,'relations_runtime':126,'sources':17,'competences':16,'packages':results,'shared_kb_hashes':hashes,'same_core_kb_across_project_packages':True,'kb_live_enabled':True,'skill_runtime_changed':True,'legal_review_required':True,'validated_at':'2026-09-12'}
    (D/'project-validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
