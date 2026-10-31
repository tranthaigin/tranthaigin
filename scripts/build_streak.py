from streak_fire import fires, fire_style
"""Generate a self-contained weekly streak panel from GitHub's full history."""
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def graphql(query, variables):
    payload = json.dumps({'query': query, 'variables': variables})
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        request = urllib.request.Request('https://api.github.com/graphql', data=payload.encode(), headers={'Authorization': 'Bearer '+token, 'Content-Type': 'application/json', 'User-Agent': 'tranthaigin-profile'})
        with urllib.request.urlopen(request, timeout=45) as response:
            result = json.load(response)
    else:
        result = json.loads(subprocess.run(['gh', 'api', 'graphql', '--input', '-'], input=payload, capture_output=True, text=True, encoding='utf-8', check=True).stdout)
    if result.get('errors'):
        raise ValueError('GitHub history query failed; keeping previous panel')
    return result['data']['user']

def statistics(days, today):
    # Sunday–Saturday UTC weeks. An unfinished empty week preserves last week's streak.
    def sunday(day):
        return day-dt.timedelta(days=(day.weekday()+1)%7)
    active = sorted({sunday(dt.date.fromisoformat(day)) for day, count in days.items() if count > 0 and dt.date.fromisoformat(day) <= today})
    longest = []; run = []
    for week in active:
        run = run+[week] if run and week-run[-1] == dt.timedelta(days=7) else [week]
        if len(run) > len(longest):
            longest = run[:]
    current = []
    cursor = sunday(today)
    if cursor not in active:
        cursor -= dt.timedelta(days=7)
    while cursor in active:
        current.insert(0, cursor)
        cursor -= dt.timedelta(days=7)
    return {'total': sum(count for day, count in days.items() if dt.date.fromisoformat(day) <= today), 'current': [str(x) for x in current], 'longest': [str(x) for x in longest]}

def render(stats, created, today):
    def span(weeks):
        if not weeks: return 'No active streak'
        start = dt.date.fromisoformat(weeks[0])
        end = min(today, dt.date.fromisoformat(weeks[-1])+dt.timedelta(days=6))
        return f'{start:%b %d, %Y} – {end:%b %d, %Y}'
    panels = ''
    for x, value, label, detail, color in [(150, f'{stats["total"]:,}', 'Total Contributions', f'{created:%b %d, %Y} – Present', '#77dbea'), (450, len(stats['current']), 'Week Streak', span(stats['current']), '#a99bff'), (750, len(stats['longest']), 'Longest Week Streak', span(stats['longest']), '#77dbea')]:
        panels += f'<text x="{x}" y="153" class="number" fill="{color}">{value}</text><text x="{x}" y="187" class="label">{label}</text><text x="{x}" y="211" class="date">{detail}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="246" viewBox="0 0 900 246" role="img" aria-labelledby="title desc">
<title id="title">Tran Thai Gin — GitHub weekly streak</title><desc id="desc">{stats['total']} total contributions, {len(stats['current'])} current active weeks, {len(stats['longest'])} longest active weeks. Updated {today}. Weeks start Sunday, UTC.</desc>
<defs><linearGradient id="edge"><stop stop-color="#274b60"/><stop offset=".5" stop-color="#8b7bcd"/><stop offset="1" stop-color="#274b60"/></linearGradient><radialGradient id="halo"><stop stop-color="#7562bf" stop-opacity=".16"/><stop offset="1" stop-color="#7562bf" stop-opacity="0"/></radialGradient><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#74c4de" stroke-opacity=".035"/></pattern></defs>
<style>{fire_style()}text{{font-family:Consolas,'Cascadia Code','Courier New',monospace;text-anchor:middle}}.number{{font-size:38px;font-weight:700}}.label{{font-size:15px;fill:#dce7f5}}.date{{font-size:11px;fill:#92a5bd}}.ring{{transform-origin:450px 116px;animation:orbit 30s linear infinite}}.pulse{{animation:pulse 6s ease-in-out infinite}}@keyframes orbit{{to{{transform:rotate(360deg)}}}}@keyframes pulse{{50%{{opacity:.45}}}}@media(prefers-reduced-motion:reduce){{.ring,.pulse{{animation:none}}}}</style>
<rect x="1" y="1" width="898" height="244" rx="18" fill="#09111f" stroke="url(#edge)"/><rect x="2" y="2" width="896" height="242" rx="18" fill="url(#grid)"/>
<path d="M20 37V20H62M838 20H880V37M20 209V226H62M838 226H880V209" fill="none" stroke="#6ccbdc" stroke-opacity=".55"/>

<path d="M300 66V207M600 66V207" stroke="#27354b"/>
{fires()}{panels}</svg>'''

def main():
    today = dt.datetime.now(dt.timezone.utc).date()
    created = dt.date.fromisoformat(graphql('query { user(login:"tranthaigin") { createdAt } }', {})['createdAt'][:10])
    days = {}
    query = '''query($from:DateTime!,$to:DateTime!) { user(login:"tranthaigin") { contributionsCollection(from:$from,to:$to) { contributionCalendar { weeks { contributionDays { date contributionCount } } } } } }'''
    for year in range(created.year, today.year+1):
        end = min(dt.date(year,12,31), today)
        user = graphql(query, {'from': f'{year}-01-01T00:00:00Z', 'to': f'{end}T23:59:59Z'})
        for week in user['contributionsCollection']['contributionCalendar']['weeks']:
            for day in week['contributionDays']:
                date = dt.date.fromisoformat(day['date'])
                if date.year == year and created <= date <= today:
                    count = day['contributionCount']
                    assert type(count) is int and count >= 0
                    days[str(date)] = count
    assert len(days) == (today-created).days+1, 'Incomplete GitHub history'
    stats = statistics(days, today)
    snapshot = {'username': 'tranthaigin', 'created': str(created), 'as_of': str(today), 'week_starts': 'Sunday UTC', 'stats': stats, 'days': days}
    (ROOT/'data/streak.json').write_text(json.dumps(snapshot, indent=2)+'\n', encoding='utf-8')
    (ROOT/'assets/streak-v3.svg').write_text(render(stats, created, today), encoding='utf-8')
    print(f'Streak: {stats["total"]} total, {len(stats["current"])} current weeks, {len(stats["longest"])} longest weeks')

if __name__ == '__main__': main()
