# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# Runtime: 58 ms, faster than 54.65% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 14.4 MB, less than 8.60% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(r: Optional[TreeNode], binary: str) -> None:
            if r:
                if not r.left and not r.right:
                    self.ans += int(binary + str(r.val), 2)
                    return

                helper(r.left, binary + str(r.val))
                helper(r.right, binary + str(r.val))

        helper(root, "")
        return self.ans
