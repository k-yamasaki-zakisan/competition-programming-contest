# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# Runtime: 101 ms, faster than 91.44% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.
# Memory Usage: 15.5 MB, less than 21.41% of Python3 online submissions for Insufficient Nodes in Root to Leaf Paths.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sufficientSubset(self, root, limit):
        if not root:
            return None
        elif self.dfs(root, limit, 0):
            return None
        else:
            return root

    def dfs(self, node: Optional[TreeNode], limit: int, total: int) -> bool:
        if node.left is None and node.right is None:
            if total + node.val < limit:
                return True
            else:
                return False
        else:
            if node.left and self.dfs(node.left, limit, total + node.val):
                node.left = None

            if node.right and self.dfs(node.right, limit, total + node.val):
                node.right = None

            if node.left is None and node.right is None:
                return True
            else:
                return False
