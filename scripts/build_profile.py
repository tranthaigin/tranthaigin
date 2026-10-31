from planet_details import saturn, surface_css
"""Adapted Nyan galaxy scene and jasineri pixel-lettering, plus custom social cards."""
from pathlib import Path
from space_events import ambient_events
import base64,datetime as dt,html,json,math,random
ROOT=Path(__file__).resolve().parents[1]
textures=json.loads((ROOT/'vendor/nyanduong/textures.json').read_text())
FONT=json.loads((ROOT/'vendor/gitartwork/font5x7.json').read_text())
LEVELS=['NONE','FIRST_QUARTILE','SECOND_QUARTILE','THIRD_QUARTILE','FOURTH_QUARTILE']
PALETTE=['#416074','#4e8dad','#42b6d9','#7fd6ef','#c3f7ff']

def write(name,content):
    p=ROOT/'assets'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8',newline='\n')

def hero():
    ambient_css,ambient_markup=ambient_events()
    galaxy='data:image/png;base64,'+base64.b64encode((ROOT/'assets/galaxy-texture.png').read_bytes()).decode()
    # Preserve the reference's self-contained foreignObject, CSS background drift,
    # texture-scrolling globe and inset-shadow spherical shading; expand the scene.
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 650" width="1200" height="650" role="img" aria-labelledby="title">
<title id="title">Hello, I'm Tran Thai Gin. Java Backend Developer. Animated spiral galaxy and orbiting worlds.</title>
<foreignObject width="1200" height="650"><div xmlns="http://www.w3.org/1999/xhtml"><style>
*{{box-sizing:border-box}}.scene{{width:1200px;height:650px;border-radius:18px;overflow:hidden;position:relative;color:white;font-family:system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:#030712 url({textures['stars']}) center/cover;isolation:isolate;animation:stars 45s ease-in-out infinite alternate}}
.shade{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(2,7,18,.9),rgba(3,7,18,.54) 45%,rgba(4,8,21,.1)),linear-gradient(0deg,#030713,transparent 40%)}}
.galaxy-plane{{position:absolute;width:910px;height:910px;left:410px;top:-145px;transform:rotate(-22deg) scaleY(.62)}}
.galaxy{{width:100%;height:100%;background:url({galaxy}) center/contain no-repeat;animation:galacticSpin 140s linear infinite;filter:drop-shadow(0 0 22px rgba(75,106,240,.18))}}
.aura{{position:absolute;width:250px;height:150px;left:745px;top:230px;border-radius:50%;background:radial-gradient(ellipse,rgba(238,215,180,.15),transparent 65%);filter:blur(25px);animation:breathe 8s ease-in-out infinite}}
.earth{{position:absolute;width:106px;height:106px;left:980px;top:447px;background:url({textures['earth']}) 0 center/auto 110%;border:1px solid #091221;border-radius:50%;box-shadow:0 0 22px #4584bc66,-12px -9px 16px #000 inset,4px 3px 10px #000 inset,-30px -20px 18px #0009 inset;animation:earthSpin 22s linear infinite,hoverEarth 13s ease-in-out infinite}}
.saturn-system{{position:absolute;left:668px;top:438px;width:90px;height:90px;animation:hoverEarth 17s ease-in-out infinite reverse;transform:rotate(-24deg)}}
.saturn{{position:absolute;inset:9px;border-radius:50%;background:repeating-linear-gradient(4deg,#8d7c67 0px,#dac9a5 6px,#c2ab8a 12px,#807365 15px);box-shadow:-18px -6px 20px #02040be0 inset,0 0 8px #dac9a533}}
.rings{{position:absolute;width:155px;height:40px;border:8px solid #a6947977;border-top-color:#9f947561;border-bottom-color:#d8ccaeaa;border-radius:50%;left:-32px;top:25px;box-shadow:0 0 0 2px #d8ccae33,0 0 0 6px #897d6544;transform:rotate(-18deg)}}
.neptune{{position:absolute;left:1095px;top:175px;width:29px;height:29px;border-radius:50%;background:linear-gradient(28deg,#152548,#598fc3,#8ec8e4);box-shadow:-9px -3px 9px #02040be0 inset;animation:hoverEarth 11s ease-in-out infinite}}
.copy{{position:absolute;left:64px;top:255px;width:690px}}.eyebrow{{font:13px Consolas,monospace;letter-spacing:4px;color:#8cbfd4;margin-bottom:35px}}.hello{{font-size:25px;font-weight:600;letter-spacing:3px;color:#c6d5ea;margin:0 0 8px;width:max-content;white-space:nowrap;animation:helloTyping 14s cubic-bezier(.22,.61,.36,1) infinite}}h1{{font-size:48px;letter-spacing:4px;line-height:1.3;margin:0;font-weight:700;text-shadow:0 3px 30px #020715;width:max-content;white-space:nowrap;animation:nameTyping 14s cubic-bezier(.22,.61,.36,1) infinite}}.role{{font:16px Consolas,monospace;letter-spacing:2px;color:#b8d6f8;margin:24px 0 12px}}.name{{font-size:16px;color:#a1b2cb;margin:0}}.chips{{position:absolute;inset:0;pointer-events:none}}.chip{{position:absolute;width:94px;height:94px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#f0f7ff;font:700 14px system-ui,sans-serif;letter-spacing:.7px;text-shadow:0 1px 5px #000;isolation:isolate;animation:chipOrbit 16s ease-in-out infinite}}.chip::before{{content:"";position:absolute;inset:0;border-radius:50%;z-index:-1;background:radial-gradient(circle at 30% 25%,#e2c397,#98734b 35%,#352b29 70%,#080e19 96%);box-shadow:inset -17px -10px 20px #000a,0 0 18px #b9a67a18;animation:chipGlow 8s ease-in-out infinite}}.chip::after{{content:"";position:absolute;left:-25%;top:34%;width:150%;height:30%;border:3px solid #c6b79166;border-top-color:#c6b79122;border-radius:50%;transform:rotate(-24deg);z-index:-1}}.chip:nth-child(1){{left:125px;top:115px;animation-delay:-2s}}.chip:nth-child(2){{left:240px;top:462px;width:114px;height:114px;font-size:12px;animation-duration:20s;animation-delay:-7s}}.chip:nth-child(2)::before{{background:radial-gradient(circle at 30% 25%,#b5d5bd,#4d8173 38%,#193c39 72%,#080e19 96%);animation-delay:-3s}}.chip:nth-child(2)::after{{border-color:#89bca855;border-top-color:#89bca822;transform:rotate(18deg)}}.chip:nth-child(3){{left:520px;top:382px;width:88px;height:88px;animation-duration:18s;animation-delay:-11s}}.chip:nth-child(3)::before{{background:radial-gradient(circle at 30% 25%,#b7dcf1,#547fae 36%,#243555 72%,#080e19 96%);animation-delay:-5s}}.chip:nth-child(3)::after{{border-color:#9db9e455;border-top-color:#9db9e422;transform:rotate(-35deg)}}.bottom{{position:absolute;bottom:35px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center;font:11px Consolas,monospace;letter-spacing:2px;color:#7997b6}}.line{{position:absolute;bottom:70px;left:64px;right:64px;height:1px;background:linear-gradient(90deg,#79dcec88,#9f83ff55,transparent)}}.dot{{display:inline-block;width:5px;height:5px;background:#8ce9dc;border-radius:50%;margin-right:9px;animation:breathe 3s ease-in-out infinite}}
@keyframes helloTyping{{0%,3%{{clip-path:inset(0 100% 0 0);opacity:0}}7%{{clip-path:inset(0 100% 0 0);opacity:1}}25%,85%{{clip-path:inset(0);opacity:1}}95%{{clip-path:inset(0);opacity:0}}100%{{clip-path:inset(0 100% 0 0);opacity:0}}}}@keyframes nameTyping{{0%,12%{{clip-path:inset(0 100% 0 0);opacity:0}}16%{{clip-path:inset(0 100% 0 0);opacity:1}}42%,85%{{clip-path:inset(0);opacity:1}}95%{{clip-path:inset(0);opacity:0}}100%{{clip-path:inset(0 100% 0 0);opacity:0}}}}@keyframes chipOrbit{{0%,100%{{transform:translate(-24px,0)}}25%{{transform:translate(0,-18px)}}50%{{transform:translate(24px,0)}}75%{{transform:translate(0,18px)}}}}@keyframes chipGlow{{0%,100%{{opacity:.65}}50%{{opacity:1}}}}@keyframes stars{{from{{background-position:50% 100%}}to{{background-position:50% 0%}}}}@keyframes galacticSpin{{to{{transform:rotate(360deg)}}}}@keyframes earthSpin{{to{{background-position:355px center}}}}@keyframes hoverEarth{{50%{{translate:0 -12px}}}}@keyframes breathe{{50%{{opacity:.45}}}}{ambient_css}{surface_css()}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style><div class="scene"><div class="shade"></div><div class="galaxy-plane"><div class="galaxy"></div></div><div class="aura"></div><div class="neptune"></div><div class="saturn-system">{saturn()}</div><div class="earth"></div><div class="chips"><span class="chip"><b>JAVA</b></span><span class="chip"><b>SPRING BOOT</b></span><span class="chip"><b>REACT</b></span></div>{ambient_markup}<div class="copy"><p class="hello">Hello, I'm</p><h1>Tran Thai Gin.</h1></div></div></div></foreignObject></svg>'''

def lettering(data):
    label='Tran Thai Gin'; step=14; left=(1200-(len(label)*6-1)*step)/2
    targets=[]
    # Adapted directly from gitartwork: ASCII index (code-32)*5, bit per row.
    # Removed upstream 8-character truncation and randomized contribution colors.
    for j,ch in enumerate(label):
        for col in range(5):
            bits=FONT[(ord(ch)-32)*5+col]
            for row in range(7):
                if bits>>row&1:targets.append((left+(j*6+col)*step,84+row*step))
    cells=[(c,d) for c,w in enumerate(data['calendar']['weeks']) for d in w['contributionDays']]
    # Keep recent active days visible in the lettering; every tile retains its date/count.
    assignment=sorted(range(len(cells)),key=lambda i:(cells[i][1]['contributionCount'],cells[i][1]['date']),reverse=True)
    destinations={idx:targets[j] for j,idx in enumerate(assignment[:len(targets)])}
    rnd=random.Random(26);body='';styles=[]
    for i,(c,d) in enumerate(cells):
        x=96+c*19;y=77+d['weekday']*17
        color=PALETTE[LEVELS.index(d['contributionLevel'])]
        if i in destinations:
            tx,ty=destinations[i];dx=tx-x;dy=ty-y;sx=rnd.randint(-130,130);sy=rnd.randint(-45,65)
            end=39+(tx/1200)*15
            styles.append(f'@keyframes p{i}{{0%,12%,100%{{transform:translate(0,0);opacity:.8}}25%{{transform:translate({sx}px,{sy}px) rotate({rnd.choice([-100,100])}deg);opacity:.25}}{end:.2f}%,82%{{transform:translate({dx}px,{dy}px) rotate(0deg);opacity:1}}94%{{transform:translate(0,0);opacity:.8}}}}.p{i}{{animation:p{i} 16s cubic-bezier(.25,.7,.25,1) infinite}}')
        else:styles.append(f'@keyframes p{i}{{0%,12%,94%,100%{{opacity:.35}}30%,85%{{opacity:0}}}}.p{i}{{animation:p{i} 16s ease-in-out infinite}}')
        body+=f'<rect class="p{i}" x="{x}" y="{y}" width="10" height="10" rx="1.8" fill="{color}"><title>{d["date"]}: {d["contributionCount"]} contributions</title></rect>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260" role="img" aria-labelledby="title"><title id="title">Tran Thai Gin — actual contribution tiles assemble into pixel lettering</title><style>{''.join(styles)}text{{font-family:Consolas,monospace}}@media(prefers-reduced-motion:reduce){{rect{{animation:none!important}}}}</style><rect width="1200" height="260" rx="16" fill="#070d19"/>{body}</svg>'''

def socials():
    # Original futuristic frames; glyphs use Simple Icons CC0 paths when available.
    icons={'facebook':('FACEBOOK','#73b5ff'),'instagram':('INSTAGRAM','#c495ff'),'telegram':('TELEGRAM','#64dcff'),'tiktok':('TIKTOK','#71f0df'),'mail':('EMAIL','#e3c899')}
    for slug,(label,color) in icons.items():
        if slug=='mail':glyph='<rect x="1.5" y="4.5" width="21" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m2 6 10 8 10-8" stroke="currentColor" stroke-width="1.5" fill="none"/>'
        else:
            import xml.etree.ElementTree as ET
            root=ET.parse(ROOT/'vendor/simple-icons'/f'{slug}.svg').getroot()
            path=root.find('{http://www.w3.org/2000/svg}path').get('d')
            glyph=f'<path d="{path}" fill="currentColor"/>'
        write(f'social/{slug}.svg',f'''<svg xmlns="http://www.w3.org/2000/svg" width="170" height="135" viewBox="0 0 170 135" role="img" aria-labelledby="title"><title id="title">{label}</title><defs><radialGradient id="a"><stop stop-color="{color}" stop-opacity=".14"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></radialGradient></defs><style>.orbit{{transform-origin:85px 57px;animation:spin 18s linear infinite}}@keyframes spin{{to{{transform:rotate(360deg)}}}}@media(prefers-reduced-motion:reduce){{.orbit{{animation:none}}}}</style><rect x="2" y="2" width="166" height="131" rx="12" fill="#09111f" stroke="#223147"/><circle cx="85" cy="57" r="50" fill="url(#a)"/><path d="M65 22 105 22 124 57 105 92 65 92 46 57Z" fill="#0c1828" stroke="{color}" stroke-opacity=".4"/><g class="orbit"><circle cx="85" cy="57" r="43" fill="none" stroke="{color}" stroke-opacity=".5" stroke-dasharray="18 100 28 124"/><circle cx="85" cy="14" r="2.3" fill="{color}"/></g><g transform="translate(68 40) scale(1.42)" color="{color}">{glyph}</g><text x="85" y="117" text-anchor="middle" font-family="Consolas,monospace" font-size="10" letter-spacing="2" fill="#c9d9e9">{label}</text></svg>''')

def main():
    data=json.loads((ROOT/'data/contributions.json').read_text(encoding='utf-8'))
    write('galaxy-hero.svg',hero());write('galaxy-hero-space-v5.svg',hero());write('gitartwork.svg',lettering(data));socials()
    write('divider.svg','<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="20" viewBox="0 0 1200 20"><defs><linearGradient id="g"><stop stop-color="#112339"/><stop offset=".4" stop-color="#7ad9eb"/><stop offset=".7" stop-color="#a18ae5"/><stop offset="1" stop-color="#112339"/></linearGradient></defs><path d="M120 10H1080" stroke="url(#g)" stroke-width="2"/></svg>')
    print('Built adapted galaxy, contribution lettering, five contact cards and separator')
if __name__=='__main__':main()
