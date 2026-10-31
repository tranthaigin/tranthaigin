"""Quiet cyan pixel flames, contained above the numerical counters."""
def fire_style():
    return '''.flame-body{transform-box:fill-box;transform-origin:center bottom;animation:fireRise 2.8s ease-in-out infinite alternate}.ember{animation:emberRise 3.8s ease-out infinite;opacity:0;transform-box:fill-box;transform-origin:center}@keyframes fireRise{0%{transform:scale(.93,1);opacity:.7}100%{transform:scale(1.06,1.09);opacity:1}}@keyframes emberRise{0%{opacity:0;transform:translate(0,0) scale(1)}25%{opacity:.65}100%{opacity:0;transform:translate(var(--dx),-31px) scale(.15) rotate(65deg)}}@media(prefers-reduced-motion:reduce){.flame-body{animation:none}.ember{animation:none;opacity:0}}'''

def fires():
    result = '<defs><linearGradient id="digital-fire" x1="0" y1="1" x2="0" y2="0"><stop stop-color="#176889"/><stop offset=".5" stop-color="#41c4df"/><stop offset="1" stop-color="#b0f2f6"/></linearGradient></defs>'
    for i,x in enumerate([150,450,750]):
        result += f'<g transform="translate({x-26} 39)"><ellipse cx="26" cy="64" rx="34" ry="8" fill="#50cee5" opacity=".06"/>'
        result += f'<g class="flame-body" style="animation-delay:-{i*.8}s"><path d="M12 64H40V58H47V42H41V29H35V39H30V22H24V6H18V22H12V35H6V47H2V57H8V61H12Z" fill="url(#digital-fire)"/><path d="M20 62H34V55H39V45H32V49H27V35H22V45H17V53H13V58H20Z" fill="#a5eef0" opacity=".72"/><path d="M8 48H15M30 26H35M34 56H42" stroke="#c4faff" opacity=".55"/></g>'
        for j,(ex,ey,size) in enumerate([(14,24,4),(33,31,3),(23,15,4),(40,39,3),(7,36,2)]):
            result += f'<rect class="ember" x="{ex}" y="{ey}" width="{size}" height="{size}" fill="#7ee4f0" style="--dx:{(j%3-1)*12}px;animation-delay:-{(j*.71+i*.57)%3.8:.2f}s"/>'
        result += '</g>'
    return result
