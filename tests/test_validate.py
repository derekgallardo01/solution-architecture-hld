import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

import validate  # noqa: E402


def _abs(rel):
    return os.path.join(ROOT, rel)


def test_example_hlds_have_no_unfilled_placeholders():
    for name in ("examples/hld-greenfield-logistics.md",
                 "examples/hld-whitford-legal.md"):
        issues = validate.lint(_abs(name))
        assert issues == [], f"{name} still has placeholders: {issues[:3]}"


def test_bare_hld_template_still_looks_like_a_template():
    issues = validate.lint(_abs("hld-template.md"))
    assert len(issues) >= 5


def test_diagram_template_mermaid_blocks_arent_flagged():
    # The diagram template contains mermaid fences with arrows like A --> B,
    # which contain '<' / '>' in node labels. Validator must skip code fences.
    issues = validate.lint(_abs("diagram-template.md"))
    # Outside the fences there should be nothing to flag.
    assert issues == []
