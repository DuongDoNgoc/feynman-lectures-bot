# False Positive Filter: The Small Fix That Saved Hours

**Date**: 2026-02-28 (implementation during 70662bc refactor)
**Severity**: Medium
**Component**: `src/renderer/math_renderer.py` (`_is_real_latex()` filter)
**Status**: Resolved

## What Happened

Implemented a filter function `_is_real_latex()` that rejects formula extraction false positives. Without it, the renderer would extract and try to render plain text or simple variable names as if they were LaTeX formulas, causing:
- Wasted rendering cycles on non-math content
- Failed renders for trivial cases ("a", "b", "E=mc2")
- Bloated math_images_json with useless entries
- Confusion during QA when formulas appeared to "not render" (they were never meant to be formulas)

The filter is simple: return True only if the formula contains actual LaTeX markup (backslash commands like `\alpha`, `\sqrt{}`, or structural elements like `^`, `_`, `{}`). Plain text and single variables are rejected.

## The Brutal Truth

This is embarrassing to admit, but the earlier version of the formula extraction was naive. It would match anything between `$...$` or `\(...\)`, including:
- Single variable names: `$a$`, `$E$`, `$k$`
- Plain numbers: `$2$`, `$3.14$`
- Common acronyms that happen to be inside dollar signs in Markdown

The parser would happily queue these for rendering, pdflatex would complain they weren't real formulas, and the entire batch would be silently dropped (logged but not visible to the user). During development, this made debugging incredibly confusing because you'd see formulas extracted, then silently vanish from the PNG output.

The breakthrough was realizing: **if it doesn't have LaTeX markup, it's not a formula**. Not a failure case—just a false positive that should be filtered at extraction time, not wasted on rendering.

## Technical Details

**Filter implementation:**
```python
def _is_real_latex(formula: str) -> bool:
    """Return True if formula contains actual LaTeX markup."""
    return bool(re.search(r'\\[a-zA-Z]+|[\^_{}]', formula))
```

The regex checks for:
- `\\[a-zA-Z]+` — LaTeX commands (`\alpha`, `\sqrt`, `\frac`, etc.)
- `[\^_{}]` — Superscript, subscript, or braces (structural elements)

**Applied in extraction:**
```python
if formula and len(formula) > 2 and _is_real_latex(formula) and formula not in seen:
    seen.add(formula)
    results.append({...})
```

The check happens in both display and inline pattern loops, catching false positives early before they're queued for rendering.

**Example filtering:**
- ✓ `$\alpha + \beta$` — has `\alpha`, `\beta` (LaTeX commands)
- ✓ `$x^2 + y^2$` — has `^` (superscript)
- ✗ `$a$` — no LaTeX markup
- ✗ `$E=mc2$` — no backslashes or structural elements
- ✗ `$3.14$` — just a number

## What We Tried

1. **No filtering** (early approach)
   - Extracted everything matching regex patterns
   - Many failed renders, wasted cycles
   - Made debugging confusing (some "formulas" vanished)

2. **Post-render filtering**: Only store successful renders
   - Still wasted time on rendering false positives
   - Harder to debug (failures are silent)

3. **Pre-extraction filtering** (final approach)
   - Fast: reject before render pipeline
   - Clear: QA sees what was filtered and why
   - Makes logs meaningful (no more silent pdflatex failures)

## Root Cause Analysis

The assumption was: **if it's between dollar signs, it's LaTeX**. This is wrong. Markdown and plain text often use dollar signs for informal math notation or acronyms. The filter corrects this by enforcing: **dollar signs only demarcate potential math; real formulas must contain LaTeX structure**.

This is a classic over-extraction problem. In NLP, it's called "recall vs precision". The original code maximized recall (catch all formulas, even false ones), but precision was terrible. The filter trades tiny recall loss (maybe one exotic formula format would be rejected) for massive precision gain (no more false positives cluttering the pipeline).

## Lessons Learned

1. **Filter early, before expensive operations**: Rendering is expensive. Extract → filter → render, not extract → render → filter.

2. **False positives are worse than false negatives**: Missing one formula is unfortunate. Rendering 50 non-formulas to find that one real formula is inefficient and confusing.

3. **Let the data guide filter design**: Look at actual false positives in logs, then design a minimal check to catch them. Don't over-engineer—a simple regex for "LaTeX markup" is sufficient.

4. **Document filter assumptions**: Add comments explaining what's being filtered and why. Future maintainers won't know why plain text is rejected without explanation.

5. **Test filters independently**: Add unit tests for `_is_real_latex()` with known true/false cases. It's small enough to test exhaustively.

## Next Steps

- Add unit tests for `_is_real_latex()` with 10-15 test cases covering edge cases
- Log statistics: "Extracted 50 potential formulas, filtered 15 false positives, rendered 35 blocks" for QA insights
- Consider making the filter regex configurable (allow users to customize what counts as LaTeX markup)
- Monitor: if users report missing formulas, audit them against the filter to see if it's too strict

## Impact

This single 2-line function eliminated an entire class of silent failures in the rendering pipeline. It's a small change that had outsized impact on debugging clarity and rendering efficiency.
