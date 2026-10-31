import math
"""Layered, self-contained planet artwork."""
def curved_surface(label, key, light, mid, dark):
    styles=[]; shapes=[]
    for j,ch in enumerate(label):
        base=(j-(len(label)-1)/2)*(0.155 if len(label)>6 else .25)
        frames=[]
        for k in range(81):
            angle=base+2*math.pi*k/80
            facing=math.cos(angle); x=85+39*math.sin(angle); y=66+8*facing
            frames.append(f'{k*1.25:.2f}%{{transform:translate({x:.3f}px,{y:.3f}px) scale({max(.04,abs(facing)):.3f},1);opacity:{max(0,min(1,facing*5)):.3f}}}')
        cls=f'{key}-glyph{j}'
        styles.append('@keyframes '+cls+'{'+''.join(frames)+'}.'+cls+'{animation:'+cls+' 36s linear infinite}')
        shapes.append(f'<g class="{cls}" font-family="Segoe UI,Arial,sans-serif" font-size="{9 if len(label)>6 else 13}" font-weight="700" text-anchor="middle"><text x=".8" y="1.2" fill="{dark}">{ch}</text><text x="0" y="0" fill="{light}">{ch}</text></g>')
    for j in range(8):
        shapes.append(f'<ellipse class="surface-line" cx="85" cy="70" rx="{4+j*5}" ry="43" fill="none" stroke="{light}" stroke-opacity=".08" style="animation-delay:-{j*4.5}s"/>')
    return '<style>'+''.join(styles)+'@media(prefers-reduced-motion:reduce){'+','.join('.'+key+'-glyph'+str(j) for j in range(len(label)))+'{animation-play-state:paused}}</style><g clip-path="url(#'+key+'-sphere)">'+''.join(shapes)+'</g>'

def tech_planet(label, key, tilt, colors, bands):
    light, mid, dark = colors
    rings = ''.join(f'<ellipse cx="85" cy="70" rx="{r}" ry="{r*.29}" stroke-width="{w}" opacity="{a}"/>' for r,w,a in bands)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" class="tech-world" width="170" height="140" viewBox="0 0 170 140">
<defs><radialGradient id="{key}-surface" cx="28%" cy="22%" r="80%"><stop stop-color="{light}"/><stop offset=".4" stop-color="{mid}"/><stop offset="1" stop-color="{dark}"/></radialGradient>
<linearGradient id="{key}-type" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{light}"/><stop offset=".45" stop-color="{light}"/><stop offset=".55" stop-color="{mid}"/><stop offset="1" stop-color="{light}"/></linearGradient>
<clipPath id="{key}-front"><rect x="0" y="70" width="170" height="70"/></clipPath><clipPath id="{key}-back"><rect width="170" height="70"/></clipPath>
<clipPath id="{key}-sphere"><circle cx="85" cy="70" r="43"/></clipPath>
<g id="{key}-belt" fill="none" stroke="{light}">{rings}<ellipse class="belt-drift" cx="85" cy="70" rx="{bands[0][0]}" ry="{bands[0][0]*.29}" stroke-width="1.6" stroke-dasharray="2 17 5 31 1 19" opacity=".75" style="animation-duration:{19+len(bands)*3}s"/></g>
</defs><g transform="rotate({tilt} 85 70)">
<use href="#{key}-belt" clip-path="url(#{key}-back)"/>
<circle cx="85" cy="70" r="43" fill="url(#{key}-surface)"/>
<g clip-path="url(#{key}-sphere)" fill="none" stroke="{light}" opacity=".07"><path d="M35 45Q85 60 135 45M35 53Q85 68 135 53M35 81Q85 96 135 81M35 88Q85 103 135 88" stroke-width="2"/></g>
{curved_surface(label,key,light,mid,dark)}
<use href="#{key}-belt" clip-path="url(#{key}-front)"/>
</g></svg>'''

def tech_planets():
    specs=[('JAVA','java',-24,('#dcc398','#96734c','#090d17'),[(74,2,.35),(69,4,.5),(63,1,.7),(58,2,.3)]),('SPRING BOOT','spring',18,('#a9d7c4','#487f73','#080e19'),[(75,1,.55),(66,2,.3),(59,1,.6)]),('REACT','react',-35,('#acd6ef','#4b759e','#090e20'),[(74,1,.3),(68,5,.38),(62,2,.6),(57,1,.3),(53,1,.2)])]
    return ''.join('<span class="chip">'+tech_planet(*spec)+'</span>' for spec in specs)

def saturn():
    return '''<svg xmlns="http://www.w3.org/2000/svg" width="170" height="130" viewBox="0 0 170 130">
<defs>
 <radialGradient id="sat-light" cx="28%" cy="24%" r="78%"><stop stop-color="#ead9b2"/><stop offset=".45" stop-color="#bba47d"/><stop offset=".73" stop-color="#75664e"/><stop offset="1" stop-color="#090d15"/></radialGradient>
 <linearGradient id="sat-shadow"><stop stop-color="#080b12" stop-opacity="0"/><stop offset=".55" stop-color="#080b12" stop-opacity=".05"/><stop offset="1" stop-color="#03060d" stop-opacity=".94"/></linearGradient>
 <filter id="sat-cloud"><feTurbulence type="fractalNoise" baseFrequency=".035 .38" numOctaves="3" seed="12"/><feColorMatrix type="saturate" values="0"/><feBlend in="SourceGraphic" mode="soft-light"/></filter>
 <clipPath id="sat-ball"><circle cx="85" cy="65" r="34"/></clipPath>
 <g id="sat-rings" fill="none" stroke="#c1af89"><ellipse cx="85" cy="65" rx="76" ry="22" stroke-width="1" opacity=".35"/><ellipse cx="85" cy="65" rx="70" ry="20" stroke-width="5" opacity=".45"/><ellipse cx="85" cy="65" rx="64" ry="18.2" stroke-width="2" opacity=".68"/><ellipse cx="85" cy="65" rx="60" ry="17" stroke-width="2" opacity=".32"/><ellipse cx="85" cy="65" rx="54" ry="15.5" stroke-width="5" opacity=".55"/><ellipse cx="85" cy="65" rx="49" ry="14" stroke-width="1" opacity=".3"/></g>
 <clipPath id="sat-front"><rect x="0" y="65" width="170" height="65"/></clipPath>
</defs><g transform="rotate(-28 85 65)"><use href="#sat-rings"/>
<circle cx="85" cy="65" r="34" fill="url(#sat-light)"/>
<g clip-path="url(#sat-ball)"><rect x="49" y="29" width="72" height="72" fill="#b6a17e" filter="url(#sat-cloud)" opacity=".24"/><path d="M48 48Q85 57 122 48M48 57Q85 65 122 57M48 73Q85 81 122 73M48 81Q85 88 122 81" fill="none" stroke="#76654e" stroke-width="2" opacity=".2"/><circle cx="85" cy="65" r="34" fill="url(#sat-shadow)"/></g>
<use href="#sat-rings" clip-path="url(#sat-front)"/></g></svg>'''

def surface_css():
    return '''.chip::before,.chip::after{display:none}.chip .tech-world{position:absolute;width:174%;height:143%;max-width:none;left:-37%;top:-21.5%;overflow:visible}.surface-line{transform-origin:85px 70px;animation:surfaceTurn 36s linear infinite}@keyframes surfaceTurn{0%,100%{transform:scaleX(1)}50%{transform:scaleX(-1)}}.belt-drift{animation:beltFlow 28s linear infinite}@keyframes beltFlow{to{stroke-dashoffset:-300}}.saturn-system{left:632px;top:414px;width:170px;height:130px;transform:none}
.chip b{display:block;font:600 13px 'Segoe UI',Arial,sans-serif;letter-spacing:1px;color:#e4dfcd;opacity:.86;transform:rotate(-24deg) scaleY(.86);text-shadow:0 1px 1px #0b101a,0 -1px 1px #ffffff28;mix-blend-mode:soft-light}
.chip:nth-child(2) b{font-size:11px;transform:rotate(18deg) scaleY(.86);color:#e0f2df}
.chip:nth-child(3) b{transform:rotate(-35deg) scaleY(.86);color:#d8eaff}
.chip::before{background-image:repeating-linear-gradient(166deg,transparent 0px,#c6ac8220 2px,transparent 5px,transparent 9px),radial-gradient(circle at 30% 25%,#e2c397,#98734b 35%,#352b29 70%,#080e19 96%)}
.blackhole{width:60px;height:60px;background:radial-gradient(circle,#000 0 27%,#06060c 28% 32%,#e0c5a9aa 34%,#a0786744 38%,#342e4930 44%,transparent 61%);box-shadow:none;transform-origin:center}
.blackhole:before{left:-17px;top:20px;width:94px;height:19px;border:0;background:radial-gradient(ellipse,transparent 28%,#ffe5cba8 32%,#d4a08099 38%,#93665766 47%,#79607722 58%,transparent 70%);transform:rotate(-19deg);box-shadow:none}
.blackhole:after{content:"";position:absolute;left:13px;top:11px;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 48% 55%,#000 56%,#08070c 62%,#d7bfa6bb 67%,#796b7355 72%,transparent 77%);box-shadow:0 -4px 7px #d4bba122}
'''
