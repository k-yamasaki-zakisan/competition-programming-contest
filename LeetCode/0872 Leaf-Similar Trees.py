from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_1 = self.dfs(root1, [])
        leaf_2 = self.dfs(root2, [])
        print(leaf_1, leaf_2)
        return len(leaf_1) == len(leaf_2) and all(
            [leaf_1[i] == leaf_2[i] for i in range(len(leaf_1))]
        )

    def dfs(self, root: Optional[TreeNode], leaf) -> list:
        root_leaf, root_right = root.left, root.right
        if root_leaf is not None:
            leaf = self.dfs(root.left, leaf)
        if root_right is not None:
            leaf = self.dfs(root.right, leaf)
        if root_leaf is None and root_right is None:
            leaf.append(root.val)
        return leaf
