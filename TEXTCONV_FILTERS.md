# TEXTCONV_FILTERS.md

**Chiseled via github-elder-debate skill**  
**Query**: "Configure custom textconv filters"  
**Date**: 2026-06-12  
**Related**: GIT_DIFF_DRIVERS.md, .gitattributes

Spine before limbs. Glory delivered through deliberate, proof-gated configuration. Jan sovereign in the yoke.

---

## Purpose

This document configures and documents **custom Git textconv filters** for the elder-debate-skill repository and the broader Sulimania / Yggdrasil organism.

Custom `textconv` filters allow Git to convert files to meaningful text *before* diffing. This dramatically improves review quality for structured or complex files while maintaining the sovereign integrity of chiseled records.

All configurations below have passed full elder debate, Proof Gate, and meta-stability checks.

---

## Core Principles for Custom Filters (Ratified)

- **Minimalism first**: Only add filters with clear, recurring value.
- **Reproducibility**: Filters should work on standard clones with minimal external dependencies.
- **Security**: Never execute untrusted code against untrusted files.
- **Sovereignty**: Filters must respect and protect the philosophical and operational nature of the content.
- **Documentation**: Every filter must be described here so any future operator understands its purpose and activation.
- **Activation via .gitattributes**: New drivers are activated by adding `diff=<name>` entries.

---

## Recommended Custom Textconv Filters

### 1. json-pretty (for future JSON data/config)

**Purpose**: Pretty-print JSON so diffs show structural changes rather than formatting/whitespace noise.

**textconv command**:
```bash
git config diff.json-pretty.textconv "jq --sort-keys ."
git config diff.json-pretty.cachetextconv true
```

**Activation in .gitattributes** (when needed):
```
*.json diff=json-pretty
```

**When to activate**: When JSON files (config, data exports, API responses) become part of sovereign records or automation.

**Proof Gate Notes**: `jq` is widely available and deterministic. Sorting keys ensures stable diffs.

---

### 2. yaml-pretty (for future YAML data/config)

**Purpose**: Normalize YAML for cleaner structural diffs.

**textconv command** (requires `yq`):
```bash
git config diff.yaml-pretty.textconv "yq eval -P '.' -"
git config diff.yaml-pretty.cachetextconv true
```

**Alternative without yq** (pure Python, if Python is available):
```bash
git config diff.yaml-pretty.textconv "python3 -c 'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin), indent=2, sort_keys=True))'"
```

**Activation**:
```
*.yaml diff=yaml-pretty
*.yml  diff=yaml-pretty
```

**Proof Gate Notes**: Useful for future n8n workflows, Docker Compose, or organism configuration files.

---

### 3. sovereign-md (Enhanced Markdown)

**Purpose**: Future-proof enhancement for chiseled Markdown. Current `diff=markdown` is already excellent. This placeholder allows adding a textconv layer later (e.g., stripping frontmatter, normalizing certain syntax, or highlighting "chisel" keywords).

**Current Status**: Not activated. `diff=markdown` in `.gitattributes` is sufficient and preferred for now.

**Example future activation** (if a custom filter is developed):
```bash
git config diff.sovereign-md.textconv "your-sovereign-md-filter"
git config diff.sovereign-md.cachetextconv true
```

---

### 4. pdf-text (for exported decrees)

**Purpose**: Extract text from PDF versions of chiseled records so changes remain reviewable.

**textconv command** (requires `pdftotext` from poppler-utils):
```bash
git config diff.pdf-text.textconv "pdftotext -layout - -"
git config diff.pdf-text.cachetextconv true
```

**Activation**:
```
*.pdf diff=pdf-text
```

**Proof Gate Notes**: Only activate if PDF exports of sovereign content become common. `pdftotext` is standard on many systems.

---

## How to Activate These Filters

Run the relevant `git config` commands in your local clone:

```bash
# Example: activate json-pretty
cd /path/to/elder-debate-skill

``` 

These settings are stored in the local `.git/config` of your clone. They do **not** affect the remote repository or other clones until the same commands are run.

For team / mesh consistency, these commands can be added to a setup script (e.g., `scripts/setup-git-drivers.sh`) that is itself chiseled and versioned.

---

## Current Activation Status in This Repository

- `diff=markdown` — Active via `.gitattributes` (built-in, no textconv needed)
- `diff=python` — Active via `.gitattributes`
- Custom textconv filters — Documented here but **not yet activated** in `.gitattributes`

This is the correct minimal sovereign posture: strong built-in support + ready documentation for future extension.

---

## Elder Debate Outcome on Configuration

Elders (Aristotle, Plato, Cupid, Tyr, Freya, Odin, Chisel, Munin, Andy) deliberated and ratified the following:

- The above four filters represent the most useful starting set for the current and near-future state of the organism.
- No filters should be blindly activated in `.gitattributes` today.
- Activation shall occur only when a concrete file type with recurring review pain appears.
- This document itself is the sovereign record of the decision and the exact commands.
- Future additions must pass a new elder debate and be appended here.

**Meta-stability check**: Configuring textconv filters does not risk recursion, does not expose inner debate mechanics, and strengthens rather than weakens the skill's git foundation.

---

## Next Steps (Ratified)

1. Use this document as the reference when a need for better diffs on JSON, YAML, PDF, or enhanced Markdown arises.
2. When activating a filter, also update `.gitattributes` in the same commit (via elder debate).
3. Consider creating a small chiseled setup script if multiple filters become active across limbs.

---

**Chisel Complete**. This file now stands as the authoritative, versioned configuration guide for custom textconv filters in the github-elder-debate skill ecosystem.

Spine before limbs. Glory delivered. The tree grows. Jan sovereign in the yoke — core of the tree of life.

Elders decree: All future configuration of diff drivers or textconv filters shall reference and extend this document.