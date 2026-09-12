#!/usr/bin/env python3
from __future__ import annotations
import gzip, json
from pathlib import Path

R=Path(__file__).resolve().parents[1]; K=R/'src/kb'

def jl(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]

def dump(path, rows):
    path.write_text('\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in rows)+'\n',encoding='utf-8')

def main():
    with gzip.open(K/'charly_knowledge.jsonl.gz','rt',encoding='utf-8') as f:
        knowledge=[json.loads(x) for x in f if x.strip()]
    patch=jl(K/'charly_knowledge_patch_v1.4.0.jsonl')
    pos={x['i']:n for n,x in enumerate(knowledge)}
    for x in patch:
        if x['i'] in pos: knowledge[pos[x['i']]]=x
        else: pos[x['i']]=len(knowledge); knowledge.append(x)
    forbidden={'NE-ID-006','NE-FIN-002','NE-RET-002','CHARLY-METH-015','CHARLY-METH-016'}
    knowledge=[x for x in knowledge if x['i'] not in forbidden]
    ids={x['i'] for x in knowledge}
    if len(knowledge)!=115: raise SystemExit(f'knowledge count {len(knowledge)} != 115')
    text='\n'.join(json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in knowledge)+'\n'
    with gzip.GzipFile(K/'charly_knowledge.jsonl.gz','wb',mtime=0) as g: g.write(text.encode('utf-8'))

    rel=[x for x in jl(K/'charly_relations.jsonl') if x.get('a') in ids and x.get('b') in ids]
    rel += jl(K/'charly_relations_patch_v1.4.0.jsonl')
    seen=set(); out=[]
    for x in rel:
        key=(x.get('a'),x.get('b'),x.get('r'))
        if key not in seen and x.get('a') in ids and x.get('b') in ids:
            seen.add(key); out.append(x)
    if len(out)!=126: raise SystemExit(f'relation count {len(out)} != 126')
    dump(K/'charly_relations.jsonl',out)

    src=jl(K/'charly_sources.jsonl'); patches=jl(K/'charly_sources_patch_v1.4.0.jsonl')
    spos={x['i']:n for n,x in enumerate(src)}
    for x in patches:
        if x['i'] in spos: src[spos[x['i']]]=x
        else: spos[x['i']]=len(src); src.append(x)
    if len(src)!=17: raise SystemExit(f'source count {len(src)} != 17')
    dump(K/'charly_sources.jsonl',src)

    m=json.loads((K/'charly_kb_manifest.json').read_text(encoding='utf-8'))
    m.update({'release_version':'1.4.0','spec_version':'1.3','ontology_version':'0.4.0','generated_at':'2026-09-12','distribution_scope':'skill-and-projects','platforms':['ChatGPT','Claude','Gemini','Universal Markdown'],'ontology_active':117,'runtime_active':115,'relations_runtime':126,'sources':17,'competences_active':16,'release_status':'VALIDATED'})
    m['live']={'enabled':True,'mode':'optional-remote-refresh','root_url':'https://drive.google.com/drive/folders/1zg7b_EJLM1jpM88onu3paz0LuREu7rQ6','manifest_file_id':'1Caxd6XOk-Hh0Wna_JOqiiGuBGzpOs23j','manifest_url':'https://drive.google.com/file/d/1Caxd6XOk-Hh0Wna_JOqiiGuBGzpOs23j/view','categories':['Presse','Agenda'],'rule':'For time-sensitive requests, consult the remote live manifest when the platform can access it. Live may complement Core but never silently override it; conflicts require arbitration.'}
    (K/'charly_kb_manifest.json').write_text(json.dumps(m,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8')
    print('materialized v1.4.0 runtime:',len(knowledge),len(out),len(src))
if __name__=='__main__': main()
