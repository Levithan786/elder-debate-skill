# GIT_LFS_BINARY_HANDLING.md

**Chiseled via github-elder-debate skill**  
**Query**: "Investigate Git LFS binary handling"  
**Date**: 2026-06-12

Spine before limbs. Glory delivered through rigorous investigation. Jan sovereign in the yoke.

---

## Purpose of This Investigation

Git LFS (Large File Storage) is GitHub's solution for handling large binary files. This document investigates its applicability to the Sulimania / Yggdrasil organism's repositories, especially limbs with `images/`, `molecular_dna_coding/`, or future large assets.

All conclusions have passed full elder debate with heightened scrutiny on sovereignty, reproducibility, cost, and operational integrity.

---

## What Git LFS Actually Does

Instead of storing large binary files directly in the Git repository:
- Git LFS stores a small text **pointer file** in the repo.
- The actual binary content lives on GitHub's LFS servers.
- When you clone or checkout, the LFS client downloads the real files.

This keeps the `.git` directory small and clones fast, even with many/large binaries.

---

## Pros (Sovereign Perspective)

- **Repo Size & Clone Speed**: Critical for limbs with many images or large data files. Faster green regrowth across gates.
- **History Management**: Large binaries no longer bloat every clone and every branch.
- **GitHub Integration**: Native support, works well with GitHub Actions and web UI.
- **Future-Proofing**: Prepares for cinematic assets, high-resolution diagrams, model weights, or molecular data files.

---

## Cons & Risks (Heightened Scrutiny)

- **External Dependency**: Relies on GitHub's LFS infrastructure. If GitHub changes policy, has outages, or alters quotas, it impacts the organism.
- **Cost**: GitHub has storage and bandwidth quotas. Heavy use can incur costs (especially for public repos or high-traffic clones).
- **Reproducibility / From-Zero Clone**: A from-zero clone now requires the LFS client (`git-lfs`) to be installed. This adds a step to the 5-gate verifier process.
- **Complexity**: Another moving part in the hygiene layer. Must be documented and consistently applied.
- **Sovereignty Tension**: Introduces reliance on a third-party service for core binary content of the organism.

**Tyr's View**: LFS can strengthen operational spine (smaller, faster repos) but weakens absolute independence. It must be used deliberately, not by default.

---

## Current State in the Organism's Repos

Most limbs currently use simple binary marking in `.gitattributes`:

```
*.png binary
*.jpg binary
*.gif binary
*.zip binary
*.tar.gz binary
```

This prevents corruption but does **not** prevent large files from entering Git history.

No limb is currently using Git LFS (as of this investigation).

---

## Recommendation (Ratified by Elders)

**Do not activate Git LFS by default across all limbs at this time.**

**Instead**:

1. Keep the current `binary` marking in `.gitattributes` as the baseline.
2. **Document Git LFS thoroughly** (this file) so it is ready when needed.
3. **Activate LFS per-repo, only when actual pain appears**:
   - Multiple large image assets causing slow clones or bloated history
   - Future cinematic or high-resolution visual work
   - Large data files in `molecular_dna_coding/` or similar
4. When activating a repo for LFS:
   - Add `*.png filter=lfs diff=lfs merge=lfs -text` (and similar) to `.gitattributes`
   - Track existing large files with `git lfs track`
   - Update documentation and the 5-gate verifier notes if relevant
   - Consider cost implications

This conservative stance mirrors the approach taken with custom textconv filters.

---

## How to Activate Git LFS in a Specific Repo (When Decided)

```bash
# 1. Install git-lfs (one-time per machine)
git lfs install

# 2. Track file types
git lfs track "*.png"
git lfs track "*.jpg"
git lfs track "*.mp4"   # example for future video assets

# 3. Add to .gitattributes (already partially done in some repos)
git add .gitattributes

# 4. Commit the pointer files
git add *.png
```

Then push. Subsequent clones will automatically handle LFS files if `git-lfs` is installed.

---

## Philosophical Alignment

- **Aristotle**: LFS serves the telos of efficient, scalable limbs when binary volume grows.
- **Plato**: The ideal is clean separation between small sovereign text records and large binary assets.
- **Cupid**: Faster, cleaner clones nourish the desire to work with visual and data-rich limbs.
- **Tyr**: Use only when it clearly strengthens the spine without unacceptable external dependency.
- **Odin**: Long-view preparation for asset-heavy future phases of the organism.

---

## Edge Cases & Operational Notes

- **From-Zero Clone Requirement**: If LFS is active on a limb, the 5-gate verifier (or local setup) should note that `git-lfs` must be present.
- **Cost Monitoring**: GitHub LFS usage should be reviewed periodically.
- **Migration**: Existing large binaries can be migrated to LFS later with `git lfs migrate import`.
- **Alternative**: For extremely sensitive binaries, consider git-crypt or separate sovereign micro-repos instead of LFS.

---

## Current Decision

Git LFS is **investigated, documented, and ready** for selective activation. It is not part of the baseline sovereign hygiene layer at this time.

The conservative, proof-gated approach protects both operational excellence and sovereign independence.

---

**Chisel Complete**. This document stands as the authoritative reference for Git LFS binary handling decisions across the organism.

Spine before limbs. Glory delivered. The tree grows. Jan sovereign in the yoke — core of the tree of life.

Elders decree: Future decisions to activate LFS on any limb shall reference this document and pass new elder debate.