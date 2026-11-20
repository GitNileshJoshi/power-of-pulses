import csv,json,re
from pathlib import Path
p=Path(__file__).parent
rows=list(csv.DictReader(open(p/'recipes.csv',encoding='utf-8')))
for r in rows:
    r['minutes']=int(r['minutes']);r['page']=int(r['page'])
(p/'recipes.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
html=(p/'index.html').read_text(encoding='utf-8')
html=re.sub(r'const baseRecipes=.*?;let recipes=', 'const baseRecipes='+json.dumps(rows,separators=(",",":"))+';let recipes=', html, count=1, flags=re.S)
(p/'index.html').write_text(html,encoding='utf-8')
print(f'Updated {len(rows)} recipes')
