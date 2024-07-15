from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        chilren_belong_parent = {}
        parents_have_chilren = defaultdict(list)
        parents = set()
        chileren = set()
        node_memo = {}
        for p, c, direction_type in descriptions:
            parents_have_chilren[p].append([c, direction_type])
            chilren_belong_parent[c] = p
            parents.add(p)
            chileren.add(c)
        for p in parents:
            if p not in chileren:
                root = p
                break
        distance = defaultdict(int)
        distance[root] = 0
        stack = deque([root])
        while len(stack):
            now = stack.popleft()
            for c, _ in parents_have_chilren[now]:
                distance[c] = distance[now] + 1
                stack.append(c)
        sort_distance = sorted(distance.items(), key=lambda x: x[1])

        while len(sort_distance):
            now, _ = sort_distance.pop()
            node = TreeNode(now)
            for c, d_type in parents_have_chilren[now]:
                if c not in node_memo:
                    continue

                if d_type == 1:
                    node.left = node_memo[c]
                else:
                    node.right = node_memo[c]
            node_memo[now] = node
        return node_memo[root]
