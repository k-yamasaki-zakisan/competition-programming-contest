from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> list:
            if root == None:
                return [0, 0]
            left_sum_num, left_cnt = helper(root.left)
            right_sum_num, right_cnt = helper(root.right)
            sum_num, sum_cnt = (
                left_sum_num + right_sum_num + root.val,
                left_cnt + right_cnt + 1,
            )
            if sum_num // sum_cnt == root.val:
                self.ans += 1
            return [sum_num, sum_cnt]

        helper(root)
        return self.ans
