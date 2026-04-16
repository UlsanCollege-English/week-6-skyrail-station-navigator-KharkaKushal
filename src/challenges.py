from __future__ import annotations
from typing import Any


class TreeNode:
    def __init__(
        self,
        value: Any,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root: TreeNode | None) -> list[Any]:
    if root is None:
        return []
    return [root.value] + preorder_values(root.left) + preorder_values(root.right)


def inorder_values(root: TreeNode | None) -> list[Any]:
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + inorder_values(root.right)


def postorder_values(root: TreeNode | None) -> list[Any]:
    if root is None:
        return []
    return postorder_values(root.left) + postorder_values(root.right) + [root.value]


def bst_contains(root: TreeNode | None, target: int) -> bool:
    if root is None:
        return False

    if target == root.value:
        return True
    elif target < root.value:
        return bst_contains(root.left, target)
    else:
        return bst_contains(root.right, target)


def bst_insert(root: TreeNode | None, value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)

    return root