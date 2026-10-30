import argparse

import datetime as dt

import html

import json

import os

from pathlib import Path

import subprocess

import urllib.request

import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

QUERY = '''query($login:String!) { user(login:$login) { contributionsCollection {
 contributionCalendar { totalContributions weeks { contributionDays {
 date contributionCount contributionLevel weekday } } } } } }'''

LEVELS = ['NONE','FIRST_QUARTILE','SECOND_QUARTILE','THIRD_QUARTILE','FOURTH_QUARTILE']

def fetch():
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    payload = {'query':QUERY,'variables':{'login':'tranthaigin'}}
    if token:
        req = urllib.request.Request('https://api.github.com/graphql',data=json.dumps(payload).encode(),headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','User-Agent':'tranthaigin-profile'})
        with urllib.request.urlopen(req,timeout=45) as res: response=json.load(res)
    else:
        p=subprocess.run(['gh','api','graphql','--input','-'],input=json.dumps(payload),capture_output=True,text=True,encoding='utf-8',check=True)
        response=json.loads(p.stdout)
    if response.get('errors'): raise ValueError('GitHub returned GraphQL errors; previous assets preserved')
    calendar=response['data']['user']['contributionsCollection']['contributionCalendar']
    validate(calendar)
    return {'username':'tranthaigin','source':'GitHub GraphQL contributionCalendar','fetched_at':dt.datetime.now(dt.timezone.utc).isoformat(),'calendar':calendar}

def validate(cal):
    days=[d for w in cal['weeks'] for d in w['contributionDays']]
    if not 350 <= len(days) <= 371: raise ValueError('Expected a full rolling contribution year')
    if len({d['date'] for d in days}) != len(days): raise ValueError('Duplicate contribution dates')
    for d in days:
        date=dt.date.fromisoformat(d['date'])
        if type(d['contributionCount']) is not int or d['contributionCount'] < 0: raise ValueError('Invalid count')
        if d['weekday'] != (date.weekday()+1)%7 or d['contributionLevel'] not in LEVELS: raise ValueError('Invalid calendar cell')
    if sum(d['contributionCount'] for d in days) != cal['totalContributions']: raise ValueError('Calendar total mismatch')

if __name__ == '__main__':
    data=fetch()
    path=ROOT/'data/contributions.json'
    path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Fetched',data['calendar']['totalContributions'],'contributions for tranthaigin')
