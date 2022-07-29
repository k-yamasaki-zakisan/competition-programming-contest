# https://leetcode.com/problems/cousins-in-binary-tree/
# Runtime: 37 ms, faster than 85.87% of Python3 online submissions for Cousins in Binary Tree.
# Memory Usage: 13.9 MB, less than 44.53% of Python3 online submissions for Cousins in Binary Tree.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.x, self.x_parent = 0, None
        self.y, self.y_parent = 0, None

    def isCousins(self, root, x: int, y: int):
        self.helper(root, None, x, y)
        return self.x == self.y and self.x_parent != self.y_parent

    def helper(self, root, parent, x: int, y: int, depth=0):
        if root is None:
            return

        if root.val == x:
            self.x, self.x_parent = depth, parent
        if root.val == y:
            self.y, self.y_parent = depth, parent
        if root.left:
            self.helper(root.left, root, x, y, depth + 1)
        if root.right:
            self.helper(root.right, root, x, y, depth + 1)
