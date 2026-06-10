[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mHMwxQwH)
# Weekly Coding #5: Skyrail Station Navigator

## Summary
This program implements tree traversals (preorder, inorder, postorder) and binary search tree operations (search and insert) for the Skyrail Station Navigator. The tree traversals visit nodes in different orders for a general binary tree, while the BST functions efficiently search and insert values following the BST property (left < root < right). The code also includes the original `analyze_lanterns` function for lantern tracking.

## Approach
- **Preorder traversal**: Visit root first, then recursively traverse left subtree, then right subtree. Implemented using recursive calls combining `[root.value] + preorder(left) + preorder(right)`.
- **Inorder traversal**: Recursively traverse left subtree, visit root, then traverse right subtree. Implemented as `inorder(left) + [root.value] + inorder(right)`.
- **Postorder traversal**: Recursively traverse left subtree, then right subtree, then visit root. Implemented as `postorder(left) + postorder(right) + [root.value]`.
- **BST search (`bst_contains`)**: Compare target with root value. If equal, return True. If target < root, search left subtree; otherwise search right subtree. Returns False if tree is empty.
- **BST insert (`bst_insert`)**: If tree is empty, create new root. If value equals root, ignore (no duplicates). If value < root, recursively insert into left subtree; otherwise insert into right subtree. Returns the root.

## Complexity

### `preorder_values`
- **Time:** O(n) where n is the number of nodes
- **Space:** O(h) where h is the height of the tree (call stack), O(n) worst case for skewed tree
- **Why:** Visits every node exactly once; recursion depth equals tree height

### `inorder_values`
- **Time:** O(n) where n is the number of nodes
- **Space:** O(h) where h is the height of the tree (call stack), O(n) worst case for skewed tree
- **Why:** Visits every node exactly once; recursion depth equals tree height

### `postorder_values`
- **Time:** O(n) where n is the number of nodes
- **Space:** O(h) where h is the height of the tree (call stack), O(n) worst case for skewed tree
- **Why:** Visits every node exactly once; recursion depth equals tree height

### `bst_contains`
- **Time:** O(h) where h is the height of the tree, O(n) worst case for skewed tree, O(log n) for balanced BST
- **Space:** O(h) for recursion stack, O(n) worst case
- **Why:** Only traverses one path from root to leaf following BST property; does not visit all nodes

### `bst_insert`
- **Time:** O(h) where h is the height of the tree, O(n) worst case for skewed tree, O(log n) for balanced BST
- **Space:** O(h) for recursion stack, O(n) worst case
- **Why:** Follows BST property down one path to find insertion point; does not visit all nodes

## Edge-Case Checklist
- [x] Empty tree traversal returns `[]` - All three traversal functions return empty list when root is None
- [x] Single-node traversal works correctly - Tested with single node, returns list with that node's value
- [x] `bst_contains` returns `False` for an empty tree - Returns False immediately when root is None
- [x] `bst_contains` returns `False` when the target is missing - Traverses down appropriate path, returns False at leaf
- [x] `bst_insert` creates a root when the tree is empty - Returns new TreeNode when root is None
- [x] `bst_insert` ignores duplicate values - Returns existing root unchanged when value equals root.value
- [x] I tested at least one deeper insert case - Tested inserting 65 into BST with 70 as right child of 60

## Assistance & Sources
- **AI used? (Y/N):** Y
- **What AI helped with:** Code review, linting fixes, test case additions, README formatting
- **Other sources used:** Course materials on tree traversals and BST operations

## Test Results
```
============================= test session starts =============================
collected 13 items

tests/test_challenges.py::test_analyze_lanterns_full_starter_data PASSED
tests/test_challenges.py::test_analyze_lanterns_empty_input PASSED
tests/test_challenges.py::test_analyze_lanterns_detects_duplicate_lanterns PASSED
tests/test_challenges.py::test_analyze_lanterns_detects_wrong_section PASSED
tests/test_challenges.py::test_analyze_lanterns_ignores_unexpected_lantern_for_wrong_section PASSED
tests/test_challenges.py::test_tree_traversals PASSED
tests/test_challenges.py::test_tree_traversals_empty PASSED
tests/test_challenges.py::test_tree_traversals_single_node PASSED
tests/test_challenges.py::test_bst_contains PASSED
tests/test_challenges.py::test_bst_contains_empty PASSED
tests/test_challenges.py::test_bst_insert PASSED
tests/test_challenges.py::test_bst_insert_empty PASSED
tests/test_challenges.py::test_bst_insert_duplicate PASSED

=========================== 13 passed in 0.11s ===========================
```