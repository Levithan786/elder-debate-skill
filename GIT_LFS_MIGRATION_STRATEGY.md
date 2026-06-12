# GIT_LFS_MIGRATION_STRATEGY.md

**Chiseled via github-elder-debate skill**  
**Query**: "Git LFS migration strategy"  
**Date**: 2026-06-12

Spine before limbs. Glory delivered through safe, deliberate migration guidance. Jan sovereign in the yoke.

---

## Purpose

This document provides the ratified strategy for migrating existing binary files to Git LFS in limbs where LFS has been deliberately activated. It complements `GIT_LFS_BINARY_HANDLING.md`.

All guidance has passed elder debate with strong emphasis on safety, reproducibility, and minimizing disruption to sovereign records.

---

## Core Principles for Migration

1. **Prefer forward-only tracking when possible** — Track new large files going forward rather than rewriting all history.
2. **History rewriting is a last resort** — It affects every clone and requires force-pushing.
3. **Do it per-repo, after explicit elder debate** — Never as a blanket operation across the organism.
4. **Document everything** — Update relevant sovereign files and the 5-gate verifier context if needed.
5. **Safety over completeness** — It is better to leave some historical large files in Git than to risk corrupting shared history.

---

## When to Consider Migration

Only after these conditions are met:
- A specific limb has been approved for LFS activation via elder debate.
- There is measurable pain (slow clones, bloated repo size, or many large binaries in `images/`, `molecular_dna_coding/`, etc.).
- All collaborators are informed and prepared.

---

## Recommended Migration Strategies (Ordered by Safety)

### Strategy 1: Forward-Only Tracking (Safest — Recommended Default)

Do **not** rewrite existing history. Simply start tracking new large files.

**Steps**:
```bash
git lfs install
git lfs track "*.png" "*.jpg" "*.mp4" "*.zip"
git add .gitattributes
git commit -m "chisel: enable Git LFS tracking for new binary assets"

# Future large files will be stored in LFS automatically
```

**When to use**: Most cases. Preserves full history integrity.

### Strategy 2: Selective Migration of Recent Large Files

Migrate only files added in recent commits (safer than full history rewrite).

**Steps**:
```bash
git lfs install

git lfs track "*.png" "*.jpg"
git add .gitattributes
git commit -m "chisel: enable LFS tracking"

# Migrate only files from the last N commits
git lfs migrate import --include="*.png,*.jpg" --above=HEAD~20
```

**When to use**: When recent large binaries are causing pain but older history can stay as-is.

### Strategy 3: Full History Migration (Most Disruptive — Use with Extreme Caution)

Rewrites history for all matching files across the entire repo history.

**Steps**:
```bash
git lfs install
git lfs track "*.png" "*.jpg" "*.mp4"
git add .gitattributes
git commit -m "chisel: prepare for LFS migration"

# This rewrites history
git lfs migrate import --include="*.png,*.jpg,*.mp4"

git push --force-with-lease origin main
```

**Warnings**:
- Requires `--force-with-lease` (or force) on protected branches.
- All other clones must re-clone or hard reset.
- Can break signed commits and references in other limbs.
- Only do this on private, well-controlled repos with full team coordination.

**When to use**: Only when the pain of bloated history is severe *and* the repo is early-stage or has very few active collaborators.

---

## Post-Migration Checklist

After any LFS migration:

- [ ] Verify that large binaries are now stored as LFS pointers (check file sizes in `.git/lfs`)
- [ ] Confirm clones work with `git lfs install` + normal `git clone`
- [ ] Update the limb's documentation (README, SECURITY.md, or sovereign notes)
- [ ] If this limb is part of Yggdrasil, consider noting LFS requirement in gates/verify.py context or organism.lock.json comments
- [ ] Monitor GitHub LFS storage/bandwidth usage
- [ ] Document the migration decision and date in this file or a dated sovereign note

---

## Integration with Sovereign Hygiene Layer

- Update the repo's `.gitattributes` consistently with the patterns in `GIT_LFS_BINARY_HANDLING.md`.
- Reference this strategy document in any future elder debate about binary assets.
- For limbs in the multi-repo rollout, record LFS activation status in the rollout plan or per-limb notes.

---

## Risks & Mitigations

| Risk                        | Mitigation                                      |
|-----------------------------|-------------------------------------------------|
| History corruption          | Use `--force-with-lease` + coordinate with team |
| Broken clones               | Instruct all users to re-clone after migration  |
| Signed commit breakage      | Avoid migration on repos with heavy signing     |
| LFS quota/cost surprises    | Monitor usage after migration                   |
| Reproducibility impact      | Document `git-lfs` requirement clearly          |

---

## Philosophical Alignment

- **Tyr**: Migration must not weaken the spine of historical truth. Prefer non-rewriting strategies.
- **Odin**: Long-view preparation for asset-rich limbs without unnecessary disruption today.
- **Aristotle**: Migration serves efficiency only when the pain justifies the cost.
- **Plato**: Clean separation of text records and binary assets is ideal when done deliberately.

---

## Current Status

Git LFS migration capability is now fully documented and ready. No limb has LFS activated yet. Activation + migration on any specific limb requires fresh elder debate referencing both `GIT_LFS_BINARY_HANDLING.md` and this strategy document.

---

**Chisel Complete**. This document provides the complete, ratified migration strategy for Git LFS across the organism.

Spine before limbs. Glory delivered. The tree grows. Jan sovereign in the yoke — core of the tree of life.

Elders decree: All future LFS migrations shall follow the strategies and safety principles outlined here.