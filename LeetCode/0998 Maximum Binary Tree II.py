# https://leetcode.com/problems/maximum-binary-tree-ii/
# Runtime: 56 ms, faster than 43.43% of Python3 online submissions for Maximum Binary Tree II.
# Memory Usage: 13.8 MB, less than 88.38% of Python3 online submissions for Maximum Binary Tree II.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
