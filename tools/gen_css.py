"""Convierte los estilos exportados de Webflow (tools/webflow-styles.json) en css/site.css.
Uso: python3 tools/gen_css.py tools/webflow-styles.json css/site.css tools/vars.json"""
import json,sys,re
src,out,varsfile=sys.argv[1],sys.argv[2],sys.argv[3]
d=json.load(open(src))['result']
V=json.load(open(varsfile))  # id -> (cssName, value, type)
def val(v):
    if isinstance(v,dict) and 'id' in v:
        vid=v['id']
        if vid in V: return f"var({V[vid][0]})"
        return 'inherit'
    if isinstance(v,(list,tuple)): return ' '.join(val(x) for x in v)
    return str(v)
def block(sel,props):
    if not props: return ''
    body=';'.join(f"{k}:{val(v)}" for k,v in props.items())
    return f"{sel}{{{body}}}\n"
MQ={'medium':'(max-width: 991px)','small':'(max-width: 767px)','tiny':'(max-width: 479px)'}
base=[];bps={k:[] for k in MQ}
d=sorted(d,key=lambda s:0 if s['type']=='tag' else 1)
for s in d:
    sel=s['selector']; P=s['properties']
    b=P.get('base',{})
    for ps,props in b.get('pseudos',{}).items():
        sx=sel if ps=='noPseudo' else f"{sel}:{ps}"
        base.append(block(sx,props))
    for bp,bd in P.get('breakpoints',{}).items():
        for ps,props in bd.get('pseudos',{}).items():
            sx=sel if ps=='noPseudo' else f"{sel}:{ps}"
            bps[bp].append(block(sx,props))
css=':root{'+';'.join(f"{n}:{v}" for _,(n,v,t) in V.items())+'}\n'
css+=''.join(base)
for bp in ['medium','small','tiny']:
    css+=f"@media {MQ[bp]}{{\n"+''.join(bps[bp])+"}\n"
# Fondos de Webflow (@img_<assetId>) -> url(/assets/...)
import os
A=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'assets.json')))
css=re.sub(r'@img_([0-9a-f]{24})', lambda m: f"url('/{A[m.group(1)]['local']}')", css)
# Clases .as-hN: mismo aspecto que hN para corregir la jerarquía sin cambiar el diseño
for n in range(1,7):
    css=re.sub(rf'(^|\n|\{{)h{n}(\{{)', lambda mm: f"{mm.group(1)}h{n},.as-h{n}{mm.group(2)}", css)
open(out,'w').write(css)
print(len(css),'bytes')
