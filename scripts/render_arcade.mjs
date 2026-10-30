// Reuse the same abozanona Galaga engine as both reference profiles.
// Feed a real saved GraphQL calendar through a sealed fetch adapter; no network,
// no upstream action analytics, no personal token reaches the renderer.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {GalagaRenderer} from '../vendor/arcade/arcade.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const snapshot=JSON.parse(fs.readFileSync(path.join(root,'data/contributions.json'),'utf8'));
globalThis.fetch=async (url,options)=>{
 if(url!=='https://api.github.com/graphql'||options?.method!=='POST')throw new Error('Network access is disabled in the offline renderer');
 const body=JSON.parse(options.body);
 if(body.variables.login!=='tranthaigin')throw new Error('Unexpected profile requested');
 return {ok:true,json:async()=>({data:{user:{contributionsCollection:{contributionCalendar:snapshot.calendar}}}})};
};
let generated='';
const game=new GalagaRenderer({platform:'github',username:'tranthaigin',gameTheme:'github-dark',githubSettings:{accessToken:'offline-snapshot'},svgCallback:s=>{generated=s},gameOverCallback:()=>{},pointsIncreasedCallback:()=>{}});
await game.start();
if(!generated.startsWith('<svg')||!generated.includes('<animate'))throw new Error('No animated output');
// Make upstream's fixed-pixel SVG responsive without changing the simulation.
const size=generated.match(/<svg width="([\d.]+)" height="([\d.]+)"/);
if(!size)throw new Error('Unexpected upstream SVG dimensions');
generated=generated.replace('<svg ',`<svg viewBox="0 0 ${size[1]} ${size[2]}" role="img" aria-label="Galaga animation of tranthaigin contributions" `);
fs.writeFileSync(path.join(root,'assets/galaga.svg'),generated);
console.log(`Rendered upstream Galaga from ${snapshot.calendar.totalContributions} contributions (${generated.length} characters)`);
