"""Quiet cyan pixel flames, contained above the numerical counters."""
def fire_style():
    return '''.flame-body{transform-box:fill-box;transform-origin:center bottom;animation:fireRise 2.8s ease-in-out infinite alternate}.ember{animation:emberRise 3.8s ease-out infinite;opacity:0;transform-box:fill-box;transform-origin:center}@keyframes fireRise{0%{transform:scale(.93,1);opacity:.7}100%{transform:scale(1.06,1.09);opacity:1}}@keyframes emberRise{0%{opacity:0;transform:translate(0,0) scale(1)}25%{opacity:.65}100%{opacity:0;transform:translate(var(--dx),-31px) scale(.15) rotate(65deg)}}@media(prefers-reduced-motion:reduce){.flame-body{animation:none}.ember{animation:none;opacity:0}}'''

def fires():
    result = '<defs><linearGradient id="digital-fire" x1="0" y1="1" x2="0" y2="0"><stop stop-color="#176889"/><stop offset=".5" stop-color="#41c4df"/><stop offset="1" stop-color="#b0f2f6"/></linearGradient></defs>'
    result += '<g transform="translate(439 27) scale(.46)"><g class="flame-body"><path d="M23 1C32 20 12 25 28 35C30 25 38 25 37 15C60 43 45 65 25 65C3 65-4 45 10 27C8 42 18 42 17 31C14 20 24 15 23 1Z" fill="url(#digital-fire)"/><path d="M25 30C38 44 38 58 25 61C12 58 15 46 25 30Z" fill="#c0f5ff"/></g>'
    for j in range(5):
        result += f'<rect class="ember" x="{12+j*5}" y="{12+j%2*8}" width="3" height="3" fill="#8fe9f3" style="--dx:{(j-2)*5}px;animation-delay:-{j*.7}s"/>'
    result += '</g>'
    result += '<g transform="translate(137 32)" fill="none" stroke="#77dbea" stroke-width="1.6"><path d="M2 7 13 1 24 7 13 13ZM2 13 13 19 24 13M2 19 13 25 24 19"/><circle class="pulse" cx="13" cy="13" r="3" fill="#77dbea"/></g>'
    result += '<g transform="translate(738 31)" fill="none" stroke="#77dbea" stroke-width="1.6"><path d="M5 2H21V12Q13 25 5 12ZM5 5H0V10Q0 15 8 15M21 5H26V10Q26 15 18 15M13 19V26M7 27H19"/><path class="pulse" d="m13 5 1.5 3 3.5.5-2.5 2.5.5 3.5-3-1.5-3 1.5.5-3.5L8 8.5l3.5-.5Z" fill="#77dbea"/></g>'
    for x in [150,450,750]:
        result += f'<g class="ring" style="transform-origin:{x}px 112px"><circle cx="{x}" cy="112" r="45" fill="none" stroke="#77dbea" stroke-opacity=".5" stroke-dasharray="55 86"/><circle cx="{x}" cy="67" r="2" fill="#9ce8ed"/></g><circle cx="{x}" cy="112" r="39" fill="none" stroke="#8297bb" stroke-opacity=".15"/>'
    return result
