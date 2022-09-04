# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Runtime: 22 ms, faster than 99.93% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
# Memory Usage: 13.8 MB, less than 75.48% of Python3 online submissions for Binary Search Tree to Greater Sum Tree. Memory Usage: 13.9 MB, less than 62.70% of Python3 online submissions for Valid Boomerang.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.num = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.right)
            root.val = self.num = root.val + self.num
            dfs(root.left)

        dfs(root)
        return root
