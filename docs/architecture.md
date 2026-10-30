# Architecture Decisions

## Goals

1. Demonstrate end-to-end capability in one coherent artifact.
2. Zero external dependencies for the web experience.
3. Code that a human engineer can immediately extend.
4. Feel premium — not “AI-generated”.

## Key Choices

### Static Site + GitHub Pages
- Instant deployment, no backend required.
- Perfect for a pure capability showcase.
- `.nojekyll` ensures assets are served correctly.

### Design System
- CSS custom properties for all colors, radii, shadows.
- Single source of truth for light / dark themes.
- Aurora gradient used as both visual identity and brand accent.

### JavaScript Philosophy
- Vanilla only. No React, no build step.
- IntersectionObserver for progressive reveal (better than scroll listeners).
- Theme preference persisted in `localStorage` and respects `prefers-color-scheme`.

### Agent Example
- Explicit tool registration (not magic).
- Clear separation of planning → execution → synthesis.
- Dataclasses for readability and type hints.
- Ready to be swapped with real LLM calls.

## Future Extensions (intentionally left open)

- Add real tool calling via an API route.
- Turn the skill cards into live interactive demos.
- Multi-page docs site with MkDocs or Astro.
- Automated visual regression tests.

---

*This document was written by Grok as part of the original delivery.*
