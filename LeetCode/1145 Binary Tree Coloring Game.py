# https://leetcode.com/problems/binary-tree-coloring-game/description/
# Beats 58.22%
# Memory 14 MB

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.f_cnt = 0
        self.s_cnt = 0
        self.t_cnt = 0

    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def dfs(root: TreeNode, target: str):
            if not root:
                return

            if root.val == x:
                dfs(root.right, "s")
                dfs(root.left, "t")
            else:
                cnt_up(target)
                dfs(root.right, target)
                dfs(root.left, target)

        def cnt_up(target):
            if target == "f":
                self.f_cnt += 1
            elif target == "s":
                self.s_cnt += 1
            elif target == "t":
                self.t_cnt += 1

        dfs(root, "f")
        return (
            n - self.f_cnt < self.f_cnt
            or n - self.s_cnt < self.s_cnt
            or n - self.t_cnt < self.t_cnt
        )
