# GIT_DIFF_DRIVERS.md

**Chiseled via github-elder-debate skill**  
**Query**: "Explore Git diff drivers"  
**Date**: 2026-06-12  
**Context**: Following the sovereign `.gitattributes` and `.gitignore` layer for Levithan786/elder-debate-skill

Spine before limbs. Glory delivered through clear, proof-gated exploration. Jan sovereign in the yoke.

---

## What Are Git Diff Drivers?

Git diff drivers are mechanisms that tell Git *how* to generate diffs for specific file types. They are activated in `.gitattributes` using the `diff=<driver>` attribute.

They exist because the default line-by-line diff is often suboptimal for:
- Structured text (Markdown, code, JSON, YAML)
- Binary files (need conversion to text first)
- Files where certain changes should be ignored or highlighted specially

Drivers improve review quality, reduce noise in pull requests, and make the history of chiseled sovereign records more readable and meaningful.

---

## How Diff Drivers Work

1. `.gitattributes` declares `diff=<name>` for matching files.
2. Git looks for a driver named `<name>`.
3. Built-in drivers (markdown, python, etc.) are used automatically.
4. Custom drivers can be defined via `git config`:
   - `diff.<driver>.command` — external diff program
   - `diff.<driver>.textconv` — command that converts the file to plain text for diffing (very powerful)
   - `diff.<driver>.binary` — treat as binary
   - `diff.<driver>.cachetextconv` — whether to cache the textconv output

This system is highly extensible and fits perfectly with proof-gated, deliberate workflows.

---

## Built-in Diff Drivers Relevant to This Repository

### `diff=markdown`
- Already active in our sovereign `.gitattributes` for `*.md` and files in `SOVEREIGN-CHISELS/`.
- GitHub and `git diff` produce significantly better output for prose:
  - Word-level highlighting instead of whole-line changes
  - Better handling of lists, headings, and formatting
  - Much more readable for long chiseled decrees, explanations, and philosophical text
- **Implication for the skill**: When reviewing changes to SKILL.md, GITIGNORE_PATTERNS_EXPLAINED.md, or any sovereign Markdown, the diff is already optimized for human (and elder) comprehension.

### `diff=python`
- Active for `*.py` files.
- Shows function and class level changes more intelligently.
- Prepares the ground for future Roh, Cartography, or other Python limbs.

### Other Useful Built-ins
- `diff=java`, `diff=perl`, `diff=ruby`, `diff=xml`, etc.
- `diff=union` — can be useful for certain configuration or data files where overlapping changes should be merged rather than conflicted.

---

## Custom Diff Drivers (textconv) — High Potential for Sovereign Use

The most powerful and under-used feature is `textconv`.

A `textconv` driver runs an external command on both the old and new versions of a file and diffs the *text output* instead of the raw file.

**Powerful Sovereign Examples**:

- **PDF / Document diffing**: Convert PDFs to text (pdftotext) so chiseled decrees exported as PDF can still be meaningfully diffed.
- **Image description diffing**: Run an image captioning or OCR tool so changes to visual assets in `images/` can be reviewed textually.
- **JSON / YAML structural diffing**: Use `jq` or `yq` to pretty-print or extract only meaningful keys, reducing noise from formatting/whitespace.
- **Sovereign-specific "chisel diff"**: A custom script that highlights only lines containing certain keywords ("chisel", "ratified", "proof gate", "Jan sovereign") or structural changes in Yggdrasil records.
- **Binary-to-text for molecular or data files** in `molecular_dna_coding/`.

**Example Configuration** (would be added via `git config --local` or in a setup script):

```bash
git config diff.sovereign-chisel.textconv "cat"   # placeholder — real version would be a smart filter
# or
# git config diff.pdf.textconv "pdftotext -layout -"
```

Then in `.gitattributes`:
```
*.pdf diff=pdf
SOVEREIGN-CHISELS/** diff=sovereign-chisel
```

**Proof Gate Consideration**: Any custom textconv must itself be versioned, auditable, and not introduce external dependencies that could compromise reproducibility or security. Elders would debate and ratify any such addition.

---

## External Diff Tools (difftool)

Separate from drivers, `git difftool` and `git mergetool` allow launching visual or advanced diff/merge programs (VS Code, Beyond Compare, Meld, etc.).

These can be configured globally or per-repo and are excellent for deep review of complex chiseled changes.

**Relevance to Elder Debate**: When a proposed change to a core file (SKILL.md, SECURITY.md, etc.) requires careful human + pantheon review, launching a high-quality difftool can support clearer deliberation before ratification.

---

## Current State in This Repository (Ratified)

Our sovereign `.gitattributes` already activates:
- `diff=markdown` on Markdown and sovereign chisel files
- `diff=python` on Python files

This is a strong, minimal, high-value foundation.

**Recommendation from this exploration**:
- Keep current drivers.
- Consider adding `diff=union` or custom textconv drivers only when a concrete need arises (e.g., frequent JSON/YAML config or PDF exports of decrees).
- Document any future custom drivers in this file or a dedicated sovereign note.
- For now, the built-in `diff=markdown` already delivers disproportionate glory for the primary content type of this repo.

---

## Philosophical & Operational Alignment

- **Aristotle (telos)**: Diff drivers serve the end of clear, reviewable change. Better diffs = better proof gates.
- **Plato (forms)**: The ideal diff for sovereign prose is word-aware and structure-respecting, not raw line noise.
- **Cupid (longings)**: Readable diffs nourish the desire to deeply engage with and refine chiseled work.
- **Tyr (spine)**: Consistent, corruption-free diff behavior protects the integrity of the historical record.
- **Freya (breath)**: Clean diffs support the very very very long breath of composition and review.
- **Odin (long view)**: Prepares the repo for future code limbs and complex assets without current over-engineering.

Diff drivers are not mere tooling — they are part of the living deliberation infrastructure of the organism.

---

## Edge Cases & Considerations

- **Performance**: textconv commands that are slow or spawn heavy processes can degrade `git diff` and `git log -p`. Cache with `cachetextconv = true` when appropriate.
- **Reproducibility**: Custom drivers should be committed or have their behavior documented so any clone can reproduce diffs.
- **Security**: Never run untrusted textconv on untrusted files. For sovereign repos this is low risk but still relevant.
- **Binary files**: Always mark truly binary content as `binary` or with an appropriate textconv; never let Git attempt textual diff on images or archives.
- **History rewrite caution**: Changing diff drivers does not rewrite past diffs, but it improves all future ones.

---

## Next Steps (Ratified by Elders)

1. The current `.gitattributes` + this exploration document now form the complete sovereign git diff strategy for the elder-debate-skill repo.
2. Future invocations involving file edits or PR reviews should consider whether enhanced diff drivers would improve clarity.
3. If a concrete need for a custom `textconv` driver emerges (e.g., for exported decrees or structured data), it shall be debated and chiseled here.

---

**Chisel Complete**. This document stands as the permanent reference for Git diff drivers in the context of the github-elder-debate skill and its sovereign repository.

Spine before limbs. Glory delivered. The tree grows. Jan sovereign in the yoke — core of the tree of life.

Elders decree: All future git-related enhancements shall reference this exploration and the living `.gitattributes`.