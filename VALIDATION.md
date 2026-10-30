# Local validation — 2026-10-30

The current revision is in `C:\tranthaigin`; the remote was empty when cloned. No existing README or GitGreen workflow was overwritten. These checks were performed locally before publication; they do not claim a hosted Actions run or live rendering verification.

Passed checks:

- Nine SVG assets parse successfully, all local README image paths exist, and all five contact targets match the user's supplied URLs/email.
- Calendar total is validated against daily counts. The snapshot used for this revision contains 240 contributions and 370 daily tiles. Every date/count is retained in the pixel-art SVG metadata.
- Actual browser inspection at 1100 px in dark/light mode and at 390 px dark mode: every image loaded; no horizontal overflow. Evidence is saved in the ignored `validation/` directory.
- Galaxy rotation changes its computed transform; social-card orbital animation is active and stops under reduced-motion settings.
- Pixel wordmark visually verified as **Tran Thai Gin**, retaining the lowercase bitmap glyphs from the original gitartwork font. Its scatter/assemble animation is preserved.
- Greeting uses Nyan's system-font family and spaced bold typography. Browser time checks confirmed hidden → partially typed → fully visible text; reduced-motion mode displays the complete text without animation. Current screenshots: `validation/hero-refined.png` and `validation/lettering-refined.png`.
- GitHub Actions YAML parses; only scheduled/manual triggers are configured. Routine generation needs no package installation. The job stages three specific generated paths and uses a normal push.
- `git diff --check` passes. Vendored Galaga source had trailing whitespace, now normalized without logic changes. Credential-pattern scan found no token/private-key patterns in deliverable files.
- Local preview endpoint returned HTTP 200 at `http://127.0.0.1:8770/preview/dark.html`.

Not yet verified: live GitHub rendering/image-proxy behavior, hosted Actions execution, branch-rule acceptance, or physical phone rendering. The hero preserves Nyan's SVG foreignObject technique, which is browser-dependent; local browser rendering is not a guarantee for every GitHub client. No remote publication is implied by these checks.

Exact source derivations and upstream license findings are in `CREDITS.md`; maintenance and workflow activation are in `MAINTENANCE.md`.
