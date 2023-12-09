from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = ""

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.helper(root)
        return self.ans[1:-1]

    def helper(self, root: Optional[TreeNode]) -> None:
        self.ans += "("
        self.ans += str(root.val) if root else ""
        if root:
            if root.left != None or root.right != None:
                self.helper(root.left)
            if root.right != None:
                self.helper(root.right)
        self.ans += ")"
