# GIT_DIFF_DRIVERS_OVERVIEW.md

**Chiseled via github-elder-debate skill**  
**Query**: "Git diff drivers overview"  
**Date**: 2026-06-12

Spine before limbs. Glory delivered. Jan sovereign in the yoke.

---

## Sovereign Git Diff Drivers Stack — High-Level Overview

This repository (`Levithan786/elder-debate-skill`) maintains a complete, proof-gated git hygiene and diff layer designed for sovereign chiseled records, cross-machine Tailscale work, and future organism limb growth.

### The Complete Stack

1. **`.gitignore`** — Exclusion hygiene  
   Protects the repository from transient, secret, and machine-specific files.

2. **`.gitattributes`** — Handling rules  
   Defines line-ending normalization, binary treatment, and activates diff drivers.

3. **`GITIGNORE_PATTERNS_EXPLAINED.md`** — Detailed rationale for exclusion rules.

4. **`GIT_DIFF_DRIVERS.md`** — Deep exploration of diff drivers and textconv.

5. **`TEXTCONV_FILTERS.md`** — Concrete configuration for custom textconv filters.

6. **`GIT_DIFF_DRIVERS_OVERVIEW.md`** (this file) — Executive summary and quick reference.

---

## What Are Git Diff Drivers?

Diff drivers tell Git *how* to compute differences for specific file types. They are activated in `.gitattributes` via `diff=<driver>`.

They replace the default line-by-line diff with smarter, structure-aware, or converted output — dramatically improving review quality for prose, code, and structured data.

---

## Current Active Drivers (in `.gitattributes`)

| File Type              | Driver              | Purpose                                      |
|------------------------|---------------------|----------------------------------------------|
| `*.md` + SOVEREIGN-CHISELS/ | `diff=markdown`    | Word-level, readable diffs for chiseled prose |
| `*.py`                 | `diff=python`       | Function/class-aware diffs for future code   |

These are active by default in every clone.

---

## Custom Textconv Capability

Advanced filters can be configured locally using `git config diff.<name>.textconv`.

Documented and ready in `TEXTCONV_FILTERS.md`:
- `json-pretty` (via `jq`)
- `yaml-pretty` (via `yq` or Python)
- `pdf-text` (via `pdftotext`)
- `sovereign-md` (placeholder for future enhancement)

**Activation policy**: Conservative. Filters are documented but only activated in `.gitattributes` when a concrete need arises, after elder debate.

---

## Why This Matters for the Organism

- **Proof Gates**: Better diffs = clearer review = stronger ratification.
- **Cross-OS Work**: Line ending normalization + consistent diffs across the tailnet.
- **Future Limbs**: Ready infrastructure for JSON, YAML, PDFs, and code.
- **Sovereign Integrity**: Protects the readability and meaning of chiseled records.

---

## Quick Reference

- Detailed exclusion rules → `.gitignore` + `GITIGNORE_PATTERNS_EXPLAINED.md`
- Handling + active drivers → `.gitattributes`
- Deep technical exploration → `GIT_DIFF_DRIVERS.md`
- Custom filter configuration → `TEXTCONV_FILTERS.md`
- This high-level overview → `GIT_DIFF_DRIVERS_OVERVIEW.md`

All files are chiseled sovereign records and should be referenced in future git-related elder debates.

---

**Chisel Complete**. This overview consolidates the full sovereign git diff driver system.

Spine before limbs. Glory delivered. The tree grows. Jan sovereign in the yoke — core of the tree of life.