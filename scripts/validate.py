from pathlib import Path
import json,re,xml.etree.ElementTree as ET
from calendar_source import validate
ROOT=Path(__file__).resolve().parents[1]
def main():
    data=json.loads((ROOT/'data/contributions.json').read_text())
    validate(data['calendar'])
    total=0
    for p in (ROOT/'assets').rglob('*.svg'):
        s=p.read_text(encoding='utf-8');root=ET.fromstring(s)
        assert root.get('viewBox'),p
        assert p.stat().st_size<2_500_000,p
        for e in root.iter():
            tag=e.tag.split('}')[-1]
            assert tag not in ['script','iframe','canvas','video','audio'],(p,tag)
            assert not any(k.lower().startswith('on') for k in e.attrib),(p,'event handler')
            if tag=='foreignObject':assert p.name in ['galaxy-hero.svg','galaxy-hero-planets-v3.svg','galaxy-hero-space-v4.svg','galaxy-hero-space-v5.svg','galaxy-hero-space-v6.svg']
            for k,v in e.attrib.items():
                if k.endswith('href') or k=='src':assert not v.startswith(('http:','https:','javascript:')),(p,'remote resource')
        total+=p.stat().st_size
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    for src in re.findall(r'src="([^"]+)"',readme):assert (ROOT/src).is_file(),src
    for target in re.findall(r'\]\(([^)]+)\)|href="([^"]+)"',readme):
        path=next(t for t in target if t)
        if not path.startswith(('https:','mailto:','#')):assert (ROOT/path).is_file(),path
    assert 'mailto:quocthaitran26062005@gmail.com' in readme
    for handle in ['https://www.facebook.com/tranthaigin','https://www.instagram.com/tranthaigin/','https://t.me/tranthaigin','https://www.tiktok.com/@tranthaigin']:assert handle in readme
    artwork=(ROOT/'assets/gitartwork.svg').read_text()
    days=[d for w in data['calendar']['weeks'] for d in w['contributionDays']]
    assert all(f'{d["date"]}: {d["contributionCount"]} contributions' in artwork for d in days)
    assert 'Tran Thai Gin' in artwork
    assert all(p.exists() for p in [ROOT/'licenses/gitartwork-BSD-3-Clause.txt',ROOT/'vendor/simple-icons/LICENSE.md'])
    print(f'PASS: {len(list((ROOT/"assets").rglob("*.svg")))} SVGs, {len(days)} real date tiles, contact links, source notices, local paths; {total:,} SVG bytes')
if __name__=='__main__':main()
