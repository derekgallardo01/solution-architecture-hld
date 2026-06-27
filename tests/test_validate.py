import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import validate  # noqa: E402


def _abs(rel):
    return os.path.join(ROOT, rel)


def test_example_hld_has_no_unfilled_placeholders():
    issues = validate.lint(_abs("examples/hld-greenfield-logistics.md"))
    assert issues == [], f"example still has placeholders: {issues[:3]}"


def test_bare_hld_template_still_looks_like_a_template():
    issues = validate.lint(_abs("hld-template.md"))
    assert len(issues) >= 5


def test_diagram_template_mermaid_blocks_arent_flagged():
    # The diagram template contains mermaid fences with arrows like A --> B,
    # which contain '<' / '>' in node labels. Validator must skip code fences.
    issues = validate.lint(_abs("diagram-template.md"))
    # Outside the fences there should be nothing to flag.
    assert issues == []
