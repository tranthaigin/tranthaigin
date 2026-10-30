"""Build a reusable spiral-galaxy texture for the adapted Nyan CSS scene.
Authoring-only (NumPy/Pillow); scheduled refresh uses the checked-in texture.
"""
from pathlib import Path
import numpy as np
from PIL import Image,ImageFilter,ImageDraw

ROOT=Path(__file__).resolve().parents[1]
N=1000
rng=np.random.default_rng(26062005)
y,x=np.mgrid[-1:1:complex(N),-1:1:complex(N)]
r=np.sqrt(x*x+y*y); theta=np.arctan2(y,x)
noise=np.zeros((N,N),dtype=float)
for size,weight in [(16,.34),(45,.27),(120,.23),(320,.16)]:
    raw=Image.fromarray((rng.random((size,size))*255).astype('uint8')).resize((N,N),Image.Resampling.BICUBIC)
    noise+=np.asarray(raw)/255*weight
phase=2*theta-7.3*np.log(r+.075)
arms=((np.cos(phase)+1)/2)**9
threads=((np.cos(phase*3+noise*5)+1)/2)**4
fall=np.exp(-r*3.8)*(1-np.clip((r-.84)/.16,0,1))
dust=(.35+noise*1.5)**2
disk=(arms*.95+threads*.08+.045)*fall*dust
core=np.exp(-(r/.105)**1.15)
halo=np.exp(-(r/.26)**1.3)*.13
rgb=np.stack([disk*.57+core*1.6+halo*1.25,disk*.72+core*1.38+halo,disk*1.3+core*1.05+halo*.9],axis=-1)
rgb=np.clip(rgb**.72*255,0,255).astype('uint8')
base=Image.fromarray(rgb,'RGB').convert('RGBA')
alpha=np.clip((rgb.max(axis=2)/255)**.65*255,0,255).astype('uint8')
base.putalpha(Image.fromarray(alpha))
stars=Image.new('RGBA',(N,N)); draw=ImageDraw.Draw(stars)
for i in range(13000):
    rad=rng.random()**.7*.9
    angle=(7.3*np.log(rad+.075)+rng.choice([0,2*np.pi]))/2+rng.normal(0,.07+.09*rad)
    px=int((.5+rad*np.cos(angle)*.5)*N);py=int((.5+rad*np.sin(angle)*.5)*N)
    if not(0<=px<N and 0<=py<N):continue
    a=int(rng.uniform(15,140)*(1-rad*.6)); color=(170,197,255,a)
    draw.point((px,py),fill=color)
    if i%300==0:draw.ellipse((px-1,py-1,px+1,py+1),fill=(215,232,255,200))
base=Image.alpha_composite(base,stars.filter(ImageFilter.GaussianBlur(.35)))
base.save(ROOT/'assets/galaxy-texture.png',optimize=True)
print('Galaxy texture:',(ROOT/'assets/galaxy-texture.png').stat().st_size,'bytes')
