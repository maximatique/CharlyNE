#!/usr/bin/env python3
from __future__ import annotations
import gzip, hashlib, json, shutil, tempfile, zipfile
from pathlib import Path, PurePosixPath

R = Path(__file__).resolve().parents[1]
N = 'charly-coach-militant-ne'
V = 'v1.4.0'
S = R / 'src' / 'skill'
K = R / 'src' / 'kb'
O = R / 'skill.zip'
D = R / 'releases' / V / 'skill.zip'
P = R / 'releases' / V / 'skill-validation-report.json'
FIXED = (2026, 9, 12, 12, 0, 0)

def read_jsonl(path: Path):
    out=[]
    for n,line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        if line.strip():
            try: out.append(json.loads(line))
            except Exception as exc: raise SystemExit(f'{path}:{n}: {exc}')
    return out

def main():
    required=[S/'SKILL.md',S/'README.md',S/'agents/openai.yaml',S/'references/author.md',S/'references/socle.md',K/'charly_competences.jsonl',K/'charly_sources.jsonl',K/'charly_relations.jsonl',K/'charly_schema.json',K/'charly_kb_manifest.json',K/'charly_knowledge.jsonl.gz']
    for path in required:
        if not path.is_file(): raise SystemExit(f'missing {path.relative_to(R)}')
    skill=(S/'SKILL.md').read_text(encoding='utf-8')
    frontmatter=skill.split('---',2)[1] if skill.startswith('---\n') else ''
    if f'name: {N}' not in frontmatter: raise SystemExit('invalid SKILL.md identity')
    if 'display_name: "CharlyNé"' not in (S/'agents/openai.yaml').read_text(encoding='utf-8'): raise SystemExit('invalid display name')
    if 'Maximatique - Bureau NÉ 13 -  Aix en Provence' not in (S/'references/author.md').read_text(encoding='utf-8'): raise SystemExit('invalid author')
    manifest=json.loads((K/'charly_kb_manifest.json').read_text(encoding='utf-8'))
    schema=json.loads((K/'charly_schema.json').read_text(encoding='utf-8'))
    expected={'release_version':'1.4.0','spec_version':'1.3','ontology_version':'0.4.0','display_name':'CharlyNé','runtime_active':115,'relations_runtime':126,'sources':17,'competences_active':16}
    if any(manifest.get(k)!=v for k,v in expected.items()): raise SystemExit(f'manifest mismatch: {manifest}')
    if schema.get('product') != N or schema.get('display_name') != 'CharlyNé': raise SystemExit('schema mismatch')
    live=manifest.get('live') or {}
    if not live.get('enabled') or not live.get('manifest_file_id'): raise SystemExit('KB Live manifest missing')
    with gzip.open(K/'charly_knowledge.jsonl.gz','rt',encoding='utf-8') as f: knowledge_text=f.read()
    knowledge=[json.loads(x) for x in knowledge_text.splitlines() if x.strip()]
    relations=read_jsonl(K/'charly_relations.jsonl'); sources=read_jsonl(K/'charly_sources.jsonl'); competences=read_jsonl(K/'charly_competences.jsonl')
    if (len(knowledge),len(relations),len(sources),len(competences)) != (115,126,17,16): raise SystemExit('runtime count mismatch')
    ids={x['i'] for x in knowledge}
    for required_id in ('NE-EDU-001','NE-EDU-002','NE-EDU-004','CHARLY-METH-018'):
        if required_id not in ids: raise SystemExit(f'missing required knowledge {required_id}')
    forbidden={'NE-ID-006','NE-FIN-002','NE-RET-002','CHARLY-METH-015','CHARLY-METH-016'}
    if ids & forbidden: raise SystemExit(f'excluded IDs leaked: {sorted(ids&forbidden)}')
    with tempfile.TemporaryDirectory() as td:
        root=Path(td)/N; (root/'agents').mkdir(parents=True); (root/'references/kb').mkdir(parents=True)
        copies={S/'SKILL.md':root/'SKILL.md',S/'README.md':root/'README.md',S/'agents/openai.yaml':root/'agents/openai.yaml',S/'references/author.md':root/'references/author.md',S/'references/socle.md':root/'references/socle.md'}
        for src,dst in copies.items(): shutil.copy2(src,dst)
        for name in ['charly_competences.jsonl','charly_sources.jsonl','charly_relations.jsonl','charly_schema.json','charly_kb_manifest.json']: shutil.copy2(K/name, root/'references/kb'/name)
        (root/'references/kb/charly_knowledge.jsonl').write_text(knowledge_text,encoding='utf-8')
        files=sorted(p for p in root.rglob('*') if p.is_file())
        if len(files)!=11: raise SystemExit(f'archive must contain 11 files, got {len(files)}')
        O.parent.mkdir(parents=True,exist_ok=True); D.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(O,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for path in files:
                name=str(PurePosixPath(N)/path.relative_to(root).as_posix()); info=zipfile.ZipInfo(name,FIXED); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16; z.writestr(info,path.read_bytes())
        shutil.copyfile(O,D)
    with zipfile.ZipFile(O) as z:
        if len(z.namelist())!=11 or z.testzip(): raise SystemExit('zip validation failed')
    data=O.read_bytes(); digest=hashlib.sha256(data).hexdigest()
    report={'release':V,'skill_identity':N,'display_name':'CharlyNé','primary_handle':'@charly','status':'PASS','spec_version':'1.3','ontology_version':'0.4.0','knowledge_runtime':115,'relations_runtime':126,'sources':17,'competences':16,'kb_live_enabled':True,'archive_entries':11,'sha256_skill_zip':digest,'size_bytes':len(data),'validated_at':'2026-09-12','legal_review_required':True}
    P.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
