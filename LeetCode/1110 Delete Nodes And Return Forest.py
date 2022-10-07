# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Runtime: 69 ms, faster than 93.40% of Python3 online submissions for Delete Nodes And Return Forest.
# Memory Usage: 14.5 MB, less than 70.87% of Python3 online submissions for Delete Nodes And Return Forest.

from typing import List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        ans = []
        set_delete = set(to_delete)
        self.dps(root, set_delete, ans, False)
        return ans

    def dps(self, node: Optional[TreeNode], to_delete: Set[int], result, hasParent):
        if not node:
            return None

        if node.val not in to_delete:
            if not hasParent:
                result.append(node)
            node.left = self.dps(node.left, to_delete, result, True)
            node.right = self.dps(node.right, to_delete, result, True)
        else:
            node.left = self.dps(node.left, to_delete, result, False)
            node.right = self.dps(node.right, to_delete, result, False)
            return None

        return node
