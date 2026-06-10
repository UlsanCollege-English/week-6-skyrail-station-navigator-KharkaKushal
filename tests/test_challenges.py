"""Starter tests for Week 9 Homework.

Run with:

    pytest -q

These tests are a starter set. You must add at least one meaningful test of
your own before submitting.
"""

from src.challenges import analyze_lanterns
from src.challenges import preorder_values, inorder_values, postorder_values
from src.challenges import bst_contains, bst_insert, TreeNode


def test_analyze_lanterns_full_starter_data():
    expected_lanterns = {
        "river-dragon",
        "blue-crane",
        "moon-rabbit",
        "gold-tiger",
        "white-lotus",
        "red-kite",
    }

    lantern_log = [
        ("river-dragon", "North Gate"),
        ("blue-crane", "River Walk"),
        ("moon-rabbit", "River Walk"),
        ("river-dragon", "North Gate"),
        ("gold-tiger", "Market Street"),
        ("silver-fox", "Market Street"),
        ("red-kite", "South Bridge"),
    ]

    correct_sections = {
        "river-dragon": "North Gate",
        "blue-crane": "River Walk",
        "moon-rabbit": "River Walk",
        "gold-tiger": "Market Street",
        "white-lotus": "Temple Road",
        "red-kite": "Temple Road",
    }

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["seen_lanterns"] == {
        "river-dragon",
        "blue-crane",
        "moon-rabbit",
        "gold-tiger",
        "silver-fox",
        "red-kite",
    }
    assert result["missing_lanterns"] == {"white-lotus"}
    assert result["unexpected_lanterns"] == {"silver-fox"}
    assert result["duplicate_lanterns"] == {"river-dragon"}
    assert result["count_by_section"] == {
        "North Gate": 2,
        "River Walk": 2,
        "Market Street": 2,
        "South Bridge": 1,
    }
    assert result["wrong_section_lanterns"] == {
        "red-kite": {
            "expected": "Temple Road",
            "actual": "South Bridge",
        }
    }


def test_analyze_lanterns_empty_input():
    result = analyze_lanterns(set(), [], {})

    assert result["seen_lanterns"] == set()
    assert result["missing_lanterns"] == set()
    assert result["unexpected_lanterns"] == set()
    assert result["duplicate_lanterns"] == set()
    assert result["count_by_section"] == {}
    assert result["wrong_section_lanterns"] == {}


def test_analyze_lanterns_detects_duplicate_lanterns():
    expected_lanterns = {"moon-rabbit"}
    lantern_log = [
        ("moon-rabbit", "River Walk"),
        ("moon-rabbit", "River Walk"),
    ]
    correct_sections = {"moon-rabbit": "River Walk"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["duplicate_lanterns"] == {"moon-rabbit"}


def test_analyze_lanterns_detects_wrong_section():
    expected_lanterns = {"red-kite"}
    lantern_log = [
        ("red-kite", "South Bridge"),
    ]
    correct_sections = {"red-kite": "Temple Road"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["wrong_section_lanterns"] == {
        "red-kite": {
            "expected": "Temple Road",
            "actual": "South Bridge",
        }
    }


def test_analyze_lanterns_ignores_unexpected_lantern_for_wrong_section():
    expected_lanterns = {"red-kite"}
    lantern_log = [
        ("silver-fox", "Market Street"),
    ]
    correct_sections = {"red-kite": "Temple Road"}

    result = analyze_lanterns(expected_lanterns, lantern_log, correct_sections)

    assert result["unexpected_lanterns"] == {"silver-fox"}
    assert result["wrong_section_lanterns"] == {}


def test_tree_traversals():
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert preorder_values(root) == [1, 2, 4, 5, 3]
    assert inorder_values(root) == [4, 2, 5, 1, 3]
    assert postorder_values(root) == [4, 5, 2, 3, 1]


def test_tree_traversals_empty():
    assert preorder_values(None) == []
    assert inorder_values(None) == []
    assert postorder_values(None) == []


def test_tree_traversals_single_node():
    root = TreeNode(42)
    assert preorder_values(root) == [42]
    assert inorder_values(root) == [42]
    assert postorder_values(root) == [42]


def test_bst_contains():
    #       40
    #      /  \
    #    20    60
    #   / \   / \
    # 10  30 50  70
    bst = TreeNode(
        40,
        TreeNode(20, TreeNode(10), TreeNode(30)),
        TreeNode(60, TreeNode(50), TreeNode(70))
    )
    assert bst_contains(bst, 50) is True
    assert bst_contains(bst, 25) is False
    assert bst_contains(bst, 40) is True
    assert bst_contains(bst, 10) is True
    assert bst_contains(bst, 70) is True


def test_bst_contains_empty():
    assert bst_contains(None, 5) is False


def test_bst_insert():
    #       40
    #      /  \
    #    20    60
    #   / \   / \
    # 10  30 50  70
    bst = TreeNode(
        40,
        TreeNode(20, TreeNode(10), TreeNode(30)),
        TreeNode(60, TreeNode(50), TreeNode(70))
    )
    bst = bst_insert(bst, 65)
    assert bst_contains(bst, 65) is True
    # Verify 65 is left child of 70
    assert bst.right.right.left.value == 65


def test_bst_insert_empty():
    bst = bst_insert(None, 10)
    assert bst.value == 10
    assert bst.left is None
    assert bst.right is None


def test_bst_insert_duplicate():
    bst = TreeNode(10)
    bst = bst_insert(bst, 10)
    # Should not create duplicate
    assert bst.value == 10
    assert bst.left is None
    assert bst.right is None
