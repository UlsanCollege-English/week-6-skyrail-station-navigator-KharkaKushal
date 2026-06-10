class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root):
    if root is None:
        return []
    return [root.value] + preorder_values(root.left) + \
        preorder_values(root.right)


def inorder_values(root):
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + \
        inorder_values(root.right)


def postorder_values(root):
    if root is None:
        return []
    return postorder_values(root.left) + postorder_values(root.right) + \
        [root.value]


def bst_contains(root, target):
    if root is None:
        return False
    if target == root.value:
        return True
    if target < root.value:
        return bst_contains(root.left, target)
    return bst_contains(root.right, target)


def bst_insert(root, value):
    if root is None:
        return TreeNode(value)
    if value == root.value:
        return root
    if value < root.value:
        root.left = bst_insert(root.left, value)
    else:
        root.right = bst_insert(root.right, value)
    return root


def analyze_lanterns(
    expected_lanterns: set[str],
    lantern_log: list[tuple[str, str]],
    correct_sections: dict[str, str],
) -> dict[str, object]:

    seen_lanterns: set[str] = set()
    seen_once: set[str] = set()
    duplicate_lanterns: set[str] = set()
    count_by_section: dict[str, int] = {}
    wrong_section_lanterns: dict[str, dict[str, str]] = {}

    for lantern, section in lantern_log:
        # Track seen lanterns
        seen_lanterns.add(lantern)

        # Detect duplicates
        if lantern in seen_once:
            duplicate_lanterns.add(lantern)
        else:
            seen_once.add(lantern)

        # Count sections
        count_by_section[section] = count_by_section.get(section, 0) + 1

        # Check wrong section (only for expected lanterns)
        if lantern in expected_lanterns:
            expected_section = correct_sections.get(lantern)
            if expected_section is not None and expected_section != section:
                if lantern not in wrong_section_lanterns:
                    wrong_section_lanterns[lantern] = {
                        "expected": expected_section,
                        "actual": section,
                    }

    missing_lanterns = expected_lanterns - seen_lanterns
    unexpected_lanterns = seen_lanterns - expected_lanterns

    return {
        "seen_lanterns": seen_lanterns,
        "missing_lanterns": missing_lanterns,
        "unexpected_lanterns": unexpected_lanterns,
        "duplicate_lanterns": duplicate_lanterns,
        "count_by_section": count_by_section,
        "wrong_section_lanterns": wrong_section_lanterns,
    }
