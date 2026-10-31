# Profile maintenance

Local checkout: `C:\tranthaigin`. Remote: `https://github.com/tranthaigin/tranthaigin.git`. The repository was empty when cloned. No existing README or GitGreen workflow was overwritten. Publication approved by the owner on 2026-10-30. Live verification results are reported separately from local validation.

## What changed from the references

- Adapted Nyan's embedded background/Earth scene into a cinematic moving spiral galaxy with multiple worlds.
- Reused the same Galaga engine as Nyan/Minh Duy, with the user's real calendar.
- Adapted gitartwork's bitmap font and pixel rendering for Tran Thai Gin, with a full grid-to-name formation sequence and actual date/count metadata.
- Replaced social PNG bubbles with five animated technology-themed SVG cards and the user's supplied destinations.

## Local refresh

```powershell
python scripts/calendar_source.py
python scripts/build_profile.py
node scripts/render_arcade.mjs
python scripts/validate.py
```

The fetcher uses `GH_TOKEN`/`GITHUB_TOKEN` or the authenticated GitHub CLI; it never writes credentials. Python standard library and Node 24 are sufficient for routine generation. The authoring-only galaxy texture script requires already-installed NumPy/Pillow; its output PNG is checked in, so CI does not install those dependencies. The Galaga library is vendored and requires no npm install.

## Preview

The ignored `preview/` folder is rendered from the actual README. A local server on port 8770 binds only to `127.0.0.1`. Dark/light pages and 390 px screenshots are provided locally. The hero deliberately preserves Nyan's `foreignObject` technique; do not confuse a local browser pass with acceptance by every GitHub image proxy/client. If a target client strips it, use a reviewed animated raster export as fallback. README alt text and the plain developer introduction remain available.

## GitHub Actions

Push the reviewed files to the profile repository's default branch, then run **Refresh galaxy profile** once from Actions. It schedules at **08:17 Asia/Saigon daily** and needs only the built-in `GITHUB_TOKEN`. No PAT or external image service is required. Branch protection may reject direct bot writes; use your repository's reviewed update policy rather than bypass protection.

On failure, no commit/push is reached, preserving the previous remote assets. Only `data/contributions.json`, `assets/galaga.svg`, and `assets/gitartwork.svg` are staged by automation. No push-trigger loop, forced updates, fake commits, or GitGreen edits. A concurrent human update causes the normal push to fail safely; rerun on the latest branch.

See [CREDITS.md](CREDITS.md) for exact source derivations and unresolved upstream redistribution permissions. Preserve all notices and references. `.reference/`, `.tools/`, preview files, and validation screenshots are local-only and ignored.

## Ambient space effects
The hero uses a sparse 120-second CSS timeline: three brief meteors, three small black holes lasting five seconds each (including fades), and one ship that jumps between six distant positions. Positions and timing are precomputed for SVG compatibility, not runtime randomness. Events do not overlap; reduced-motion mode hides them. The current README uses a new versioned image path to refresh GitHub caches.
# Weekly streak panel

`python scripts/build_streak.py` fetches contribution history from the account creation date using GitHub GraphQL and generates `data/streak.json` and `assets/streak-v4.svg`. The daily workflow updates both. Total Contributions counts the full returned history, not only the rolling year used by the arcade. Weeks run Sunday–Saturday in UTC; one or more contributions makes a week active. An unfinished empty current week preserves the previous week's streak until that week finishes. Dates beneath streaks show week boundaries, capped at the snapshot date. Equal longest runs retain the earliest run. `python scripts/test_streak.py` checks boundaries, gaps, and empty history.
