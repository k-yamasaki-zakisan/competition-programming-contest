# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Runtime: 54 ms, faster than 72.95% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
# Memory Usage: 20 MB, less than 41.76% of Python3 online submissions for Maximum Difference Between Node and Ancestor.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = -1

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], max_num: int, min_num: int):
            if root:
                self.ans = max(
                    self.ans, abs(max_num - root.val), abs(min_num - root.val)
                )
                helper(root.left, max(root.val, max_num), min(root.val, min_num))
                helper(root.right, max(root.val, max_num), min(root.val, min_num))

        helper(root, root.val, root.val)
        return self.ans
