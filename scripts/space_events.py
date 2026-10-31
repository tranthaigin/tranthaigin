from ship_model import spacecraft
"""Sparse, deterministic pseudo-random scene events; no JavaScript inside SVG."""
import random

def ambient_events(include_cinematics=False):
    rng=random.Random(26062005)
    duration=120
    def pct(t):return f'{t/duration*100:.5f}%'
    css=['.meteor,.blackhole,.jump-ship{position:absolute;pointer-events:none;opacity:0}.meteor{width:95px;height:2px;background:linear-gradient(90deg,transparent,#b5d9ed99);border-radius:50%;transform:rotate(24deg)}.blackhole{width:35px;height:35px;border-radius:50%;background:radial-gradient(circle,#010207 38%,#060912 48%,#9281af55 53%,transparent 68%);box-shadow:0 0 12px #9083aa18}.blackhole:before{content:"";position:absolute;left:-12px;top:9px;width:57px;height:15px;border:2px solid #ba98d466;border-radius:50%;transform:rotate(-25deg)}.jump-ship{width:60px;height:36px}.jump-ship:after{content:"";position:absolute;right:26px;top:10px;width:44px;height:2px;background:linear-gradient(90deg,transparent,#7bbbe688);transform-origin:right center;animation:jumpTrail 120s linear infinite}']
    markup=[]
    for i,(start,x,y) in enumerate([(6,470,45),(38,800,40),(80,440,90)]):
        x+=rng.randint(-25,25)
        css.append(f'@keyframes meteor{i}{{0%,{pct(start)}{{opacity:0;transform:translate(0,0) rotate(24deg)}}{pct(start+.25)}{{opacity:.6}}{pct(start+1.2)}{{opacity:0;transform:translate(230px,100px) rotate(24deg)}}100%{{opacity:0;transform:translate(230px,100px) rotate(24deg)}}}}.meteor.m{i}{{left:{x}px;top:{y}px;animation:meteor{i} 120s linear infinite}}')
        markup.append(f'<div class="meteor m{i}"></div>')
    if include_cinematics:
        from cinematic_events import cinematic
        extra_css, extra_markup = cinematic()
        return ''.join(css)+extra_css, ''.join(markup)+extra_markup
    return ''.join(css), ''.join(markup)
