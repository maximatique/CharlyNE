#!/usr/bin/env python3
from __future__ import annotations
import gzip, hashlib, json, shutil, tempfile, zipfile
from pathlib import Path, PurePosixPath

R=Path(__file__).resolve().parents[1]; N='charly-coach-militant-ne'; V='v1.3.0'
S=R/'src/skill'; K=R/'src/kb'; O=R/'skill.zip'; D=R/'releases'/V/'skill.zip'; P=R/'releases'/V/'validation-report.json'
FIXED=(2026,9,6,12,0,0)

def jl(p):
    out=[]
    for n,x in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
        if x.strip():
            try: out.append(json.loads(x))
            except Exception as e: raise SystemExit(f'{p}:{n}: {e}')
    return out

def main():
    req=[S/'SKILL.md',S/'README.md',S/'agents/openai.yaml',S/'references/author.md',S/'references/socle.md',K/'charly_competences.jsonl',K/'charly_sources.jsonl',K/'charly_relations.jsonl',K/'charly_schema.json',K/'charly_kb_manifest.json',K/'charly_knowledge.jsonl.gz',R/'tests/reference_tests.jsonl']
    for p in req:
        if not p.is_file(): raise SystemExit(f'missing {p.relative_to(R)}')
    skill=(S/'SKILL.md').read_text(encoding='utf-8')
    if not skill.startswith('---\n') or f'name: {N}' not in skill.split('---',2)[1]: raise SystemExit('invalid SKILL.md identity')
    if 'display_name: "CharlyNé"' not in (S/'agents/openai.yaml').read_text(encoding='utf-8'): raise SystemExit('invalid display name')
    if 'Maximatique - Bureau NÉ 13 -  Aix en Provence' not in (S/'references/author.md').read_text(encoding='utf-8'): raise SystemExit('invalid author')
    m=json.loads((K/'charly_kb_manifest.json').read_text(encoding='utf-8')); sc=json.loads((K/'charly_schema.json').read_text(encoding='utf-8'))
    expected={'release_version':'1.3.0','ontology_version':'0.3.0','display_name':'CharlyNé','runtime_active':113,'relations_runtime':126,'sources':16,'competences_active':16,'distribution_scope':'standalone-skill'}
    if any(m.get(k)!=v for k,v in expected.items()) or sc.get('product')!=N or sc.get('display_name')!='CharlyNé': raise SystemExit('manifest/schema mismatch')
    with gzip.open(K/'charly_knowledge.jsonl.gz','rt',encoding='utf-8') as f: kt=f.read()
    know=[json.loads(x) for x in kt.splitlines() if x.strip()]; rel=jl(K/'charly_relations.jsonl'); src=jl(K/'charly_sources.jsonl'); comp=jl(K/'charly_competences.jsonl'); tests=jl(R/'tests/reference_tests.jsonl')
    if (len(know),len(rel),len(src),len(comp),len(tests))!=(113,126,16,16,40): raise SystemExit('count mismatch')
    ids={x['i'] for x in know}; forbidden={'CHARLY-METH-015','CHARLY-METH-016','NE-ID-006','NE-FIN-002','NE-RET-002'}
    if ids & forbidden: raise SystemExit(f'excluded IDs leaked: {sorted(ids&forbidden)}')
    missing=[(t['id'],i) for t in tests for i in t.get('expected_ids',[]) if i not in ids]
    if missing: raise SystemExit(f'test IDs missing: {missing}')
    rt=(K/'charly_relations.jsonl').read_text(encoding='utf-8')
    bad=[x for x in ['NE-CUNT-','¨0','Átat-performance','"d":"’'] if x in rt]
    if bad: raise SystemExit(f'corrupt relation markers: {bad}')
    with tempfile.TemporaryDirectory() as td:
        b=Path(td)/N; (b/'agents').mkdir(parents=True); (b/'references/kb').mkdir(parents=True)
        copies={S/'SKILL.md':b/'SKILL.md',S/'README.md':b/'README.md',S/'agents/openai.yaml':b/'agents/openai.yaml',S/'references/author.md':b/'references/author.md',S/'references/socle.md':b/'references/socle.md'}
        for a,z in copies.items(): shutil.copy2(a,z)
        for n in ['charly_competences.jsonl','charly_sources.jsonl','charly_relations.jsonl','charly_schema.json','charly_kb_manifest.json']: shutil.copy2(K/n,b/'references/kb'/n)
        (b/'references/kb/charly_knowledge.jsonl').write_text(kt,encoding='utf-8')
        files=sorted(p for p in b.rglob('*') if p.is_file())
        if len(files)!=11: raise SystemExit('archive must contain 11 files')
        O.parent.mkdir(parents=True,exist_ok=True); D.parent.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(O,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
            for p in files:
                name=str(PurePosixPath(N)/p.relative_to(b).as_posix()); info=zipfile.ZipInfo(name,FIXED); info.compress_type=zipfile.ZIP_DEFLATED; info.external_attr=0o100644<<16; z.writestr(info,p.read_bytes())
        shutil.copyfile(O,D)
    with zipfile.ZipFile(O) as z:
        if len(z.namelist())!=11 or {PurePosixPath(x).parts[0] for x in z.namelist()}!={N} or z.testzip(): raise SystemExit('zip validation failed')
    data=O.read_bytes(); h=hashlib.sha256(data).hexdigest()
    if len(data)>25*1024*1024 or D.read_bytes()!=data: raise SystemExit('distribution mismatch')
    report={'release':V,'skill_identity':N,'display_name':'CharlyNé','primary_handle':'@charly','status':'PASS','skill_validator':'PASS','repository_package_validation':'PASS','reference_tests':'40/40 expected identifiers present','knowledge_runtime':113,'relations_runtime':126,'sources':16,'competences':16,'excluded_master_active_by_scope':['CHARLY-METH-015','CHARLY-METH-016'],'excluded_arbitration_ids':['NE-ID-006','NE-FIN-002','NE-RET-002'],'contains_project_package':False,'contains_xlsx':False,'contains_internal_arbitrages_or_backlog':False,'archive_entries':11,'sha256_skill_zip':h,'size_bytes':len(data),'validated_at':'2026-09-06','legal_review_required':True}
    P.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
