# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Runtime: 74 ms, faster than 16.85% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
# Memory Usage: 13.9 MB, less than 53.49% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not len(preorder):
            return None
        targe = TreeNode(preorder[0])
        i = 1
        while i < len(preorder):
            if preorder[0] < preorder[i]:
                break
            i += 1
        targe.left = self.bstFromPreorder(preorder[1:i])
        targe.right = self.bstFromPreorder(preorder[i:])
        return targe
