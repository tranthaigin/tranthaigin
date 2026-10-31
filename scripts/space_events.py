from ship_model import spacecraft
"""Sparse, deterministic pseudo-random scene events; no JavaScript inside SVG."""
import random

def ambient_events():
    rng=random.Random(26062005)
    duration=120
    def pct(t):return f'{t/duration*100:.5f}%'
    css=['.meteor,.blackhole,.jump-ship{position:absolute;pointer-events:none;opacity:0}.meteor{width:95px;height:2px;background:linear-gradient(90deg,transparent,#b5d9ed99);border-radius:50%;transform:rotate(24deg)}.blackhole{width:35px;height:35px;border-radius:50%;background:radial-gradient(circle,#010207 38%,#060912 48%,#9281af55 53%,transparent 68%);box-shadow:0 0 12px #9083aa18}.blackhole:before{content:"";position:absolute;left:-12px;top:9px;width:57px;height:15px;border:2px solid #ba98d466;border-radius:50%;transform:rotate(-25deg)}.jump-ship{width:60px;height:36px}.jump-ship:after{content:"";position:absolute;right:26px;top:10px;width:44px;height:2px;background:linear-gradient(90deg,transparent,#7bbbe688);transform-origin:right center;animation:jumpTrail 120s linear infinite}']
    markup=[]
    for i,(start,x,y) in enumerate([(6,470,45),(38,800,40),(80,440,90)]):
        x+=rng.randint(-25,25)
        css.append(f'@keyframes meteor{i}{{0%,{pct(start)}{{opacity:0;transform:translate(0,0) rotate(24deg)}}{pct(start+.25)}{{opacity:.6}}{pct(start+1.2)}{{opacity:0;transform:translate(230px,100px) rotate(24deg)}}100%{{opacity:0;transform:translate(230px,100px) rotate(24deg)}}}}.meteor.m{i}{{left:{x}px;top:{y}px;animation:meteor{i} 120s linear infinite}}')
        markup.append(f'<div class="meteor m{i}"></div>')
    for i,(start,x,y) in enumerate([(14,585,125),(52,1105,325),(100,730,565)]):
        css.append(f'@keyframes hole{i}{{0%,{pct(start)},{pct(start+5)},100%{{opacity:0;transform:scale(.7)}}{pct(start+1.2)},{pct(start+3.5)}{{opacity:.65;transform:scale(1)}}}}.blackhole.b{i}{{left:{x}px;top:{y}px;animation:hole{i} 120s ease-in-out infinite}}')
        markup.append(f'<div class="blackhole b{i}"></div>')
    # Exactly one ship element. It disappears completely before changing position.
    stops=[(25,450,180),(29,1050,70),(67,770,550),(71,420,55),(90,1125,390),(94,575,580)]
    frames=['0%{opacity:0;transform:translate(450px,180px) scaleX(.2)}']
    trails=['0%,100%{opacity:0}']
    for t,x,y in stops:
        frames += [f'{pct(t)}{{opacity:0;transform:translate({x}px,{y}px) scaleX(2.4)}}',f'{pct(t+.3)}{{opacity:.75;transform:translate({x}px,{y}px) scaleX(1)}}',f'{pct(t+1.8)}{{opacity:.75;transform:translate({x+12}px,{y-3}px) scaleX(1)}}',f'{pct(t+2.15)}{{opacity:0;transform:translate({x+50}px,{y-5}px) scaleX(3)}}']
        trails += [f'{pct(t)},{pct(t+2.15)}{{opacity:0}}',f'{pct(t+.12)},{pct(t+1.95)}{{opacity:.55}}',f'{pct(t+.45)},{pct(t+1.7)}{{opacity:.08}}']
    frames.append('100%{opacity:0;transform:translate(625px,575px) scaleX(3)}')
    css.append('@keyframes alphaJump{'+''.join(frames)+'}.jump-ship{left:0;top:0;animation:alphaJump 120s linear infinite}@keyframes jumpTrail{'+''.join(trails)+'}')
    markup.append('<div class="jump-ship">'+spacecraft()+'</div>')
    return ''.join(css),''.join(markup)
