"""Precomputed cinematic choreography, one ship and sparse independent scenes."""
import math
from ship_model import spacecraft

def cinematic():
    def pct(t): return f'{t/120*100:.4f}%'
    css=['.rift,.gravity{position:absolute;opacity:0;pointer-events:none}.rift{width:38px;height:90px;border-radius:50%;background:repeating-radial-gradient(ellipse,#010612 0 4px,#4584a54d 5px,#081326 8px);box-shadow:0 0 9px #83d6ff88,inset 0 0 7px #c1eaff;border:1px solid #94dafa99}.gravity{width:200px;height:170px}.gravity svg{overflow:visible}.jump-ship{width:60px;height:36px}.jump-ship:after{display:none}']
    markup=[]
    frames=['0%{opacity:0;transform:translate(400px,160px)}']
    for i,(t,x,y,ex,ey) in enumerate([(25,400,160,960,60),(66,390,490,910,220),(88,470,70,820,510)]):
        for suffix,begin,px,py in [('in',t+1,x+180,y-26),('out',t+4,ex,ey-26)]:
            name=f'rift{i}{suffix}'
            css.append(f'@keyframes {name}{{0%,{pct(begin)},100%{{opacity:0;transform:scale(.03)}}{pct(begin+.7)},{pct(begin+2)}{{opacity:.85;transform:scale(1)}}{pct(begin+3)}{{opacity:0;transform:scale(.03)}}}}.{name}{{left:{px}px;top:{py}px;animation:{name} 120s ease-in-out infinite}}')
            markup.append(f'<div class="rift {name}"></div>')
        for time,px,py,scale,opacity in [(t,x,y,1,0),(t+.5,x+10,y,1,1),(t+2,x+45,y,1,1),(t+3,x+170,y,.18,0),(t+4,ex,ey,.12,0),(t+4.4,ex+12,ey,.6,1),(t+5,ex+45,ey,.65,1),(t+8,ex+130,ey-12,.55,.8),(t+10,ex+230,ey-24,.35,0)]:
            frames.append(f'{pct(time)}{{opacity:{opacity};transform:translate({px}px,{py}px) scale({scale})}}')
    frames.append('100%{opacity:0;transform:translate(1050px,486px) scale(.35)}')
    css.append('@keyframes alphaJump{'+''.join(frames)+'}.jump-ship{left:0;top:0;animation:alphaJump 120s linear infinite}')
    markup.append('<div class="jump-ship">'+spacecraft()+'</div>')
    for i,(t,x,y) in enumerate([(12,520,45),(48,940,300),(103,620,435)]):
        name=f'gravity{i}'
        css.append(f'@keyframes {name}{{0%,{pct(t)},100%{{opacity:0;transform:scale(.02)}}{pct(t+2)}{{opacity:.9;transform:scale(1)}}{pct(t+6)}{{opacity:.9;transform:scale(1)}}{pct(t+8)}{{opacity:.5;transform:scale(.12)}}{pct(t+9)}{{opacity:0;transform:scale(.01)}}}}.{name}{{left:{x}px;top:{y}px;animation:{name} 120s ease-in-out infinite}}')
        stars=''
        for j in range(22):
            angle=j*2.399; radius=65+j%4*10; points=[]
            for k in range(13):
                f=k/12; r=radius*(1-f); a=angle+f*f*6
                points.append(f'{pct(t+1+j%4*.3+f*5)}{{transform:translate({100+r*math.cos(a):.2f}px,{85+r*.7*math.sin(a):.2f}px);opacity:{1-f:.3f}}}')
            cls=f'dust{i}_{j}'
            css.append('@keyframes '+cls+'{0%,100%{opacity:0}'+''.join(points)+'}.'+cls+'{animation:'+cls+' 120s linear infinite}')
            stars+=f'<circle class="{cls}" r="{.7+j%3*.4}" fill="#d6e4ef"/>'
        markup.append(f'''<div class="gravity {name}"><svg xmlns="http://www.w3.org/2000/svg" width="200" height="170" viewBox="0 0 200 170"><defs><radialGradient id="g{i}"><stop stop-color="#000"/><stop offset=".5" stop-color="#03040a"/><stop offset=".56" stop-color="#dec3a1"/><stop offset=".60" stop-color="#795b4d" stop-opacity=".5"/><stop offset="1" stop-color="#353354" stop-opacity="0"/></radialGradient></defs><ellipse cx="100" cy="85" rx="94" ry="69" fill="none" stroke="#a0b7d5" stroke-opacity=".12" stroke-width="4"/>{stars}<circle cx="100" cy="85" r="52" fill="url(#g{i})"/><ellipse cx="100" cy="85" rx="83" ry="18" fill="none" stroke="#ab8060" stroke-opacity=".3" stroke-width="9"/><ellipse cx="100" cy="85" rx="79" ry="15" fill="none" stroke="#e5c9a5" stroke-opacity=".65" stroke-width="2"/><circle cx="100" cy="82" r="26" fill="#010207"/><path d="M69 83C68 34 132 34 131 83" fill="none" stroke="#d5bc9e" stroke-width="2" opacity=".7"/><path d="M23 86Q100 111 177 86" fill="none" stroke="#eed4b2" stroke-width="2" opacity=".65"/></svg></div>''')
    return ''.join(css),''.join(markup)
