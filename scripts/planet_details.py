"""Layered, self-contained planet artwork."""
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
    return '''.saturn-system{left:632px;top:414px;width:170px;height:130px;transform:none}
.chip b{display:block;font:600 13px 'Segoe UI',Arial,sans-serif;letter-spacing:1px;color:#e4dfcd;opacity:.86;transform:rotate(-24deg) scaleY(.86);text-shadow:0 1px 1px #0b101a,0 -1px 1px #ffffff28;mix-blend-mode:soft-light}
.chip:nth-child(2) b{font-size:11px;transform:rotate(18deg) scaleY(.86);color:#e0f2df}
.chip:nth-child(3) b{transform:rotate(-35deg) scaleY(.86);color:#d8eaff}
.chip::before{background-image:repeating-linear-gradient(166deg,transparent 0px,#c6ac8220 2px,transparent 5px,transparent 9px),radial-gradient(circle at 30% 25%,#e2c397,#98734b 35%,#352b29 70%,#080e19 96%)}
.blackhole{width:60px;height:60px;background:radial-gradient(circle,#000 0 27%,#06060c 28% 32%,#e0c5a9aa 34%,#a0786744 38%,#342e4930 44%,transparent 61%);box-shadow:none;transform-origin:center}
.blackhole:before{left:-17px;top:20px;width:94px;height:19px;border:0;background:radial-gradient(ellipse,transparent 28%,#ffe5cba8 32%,#d4a08099 38%,#93665766 47%,#79607722 58%,transparent 70%);transform:rotate(-19deg);box-shadow:none}
.blackhole:after{content:"";position:absolute;left:13px;top:11px;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 48% 55%,#000 56%,#08070c 62%,#d7bfa6bb 67%,#796b7355 72%,transparent 77%);box-shadow:0 -4px 7px #d4bba122}
'''
