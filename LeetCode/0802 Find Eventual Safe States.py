from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        memo = [0] * n  # 0: unvisited, 1: safe, -1: unsafe
        res = []

        def dfs(node):
            if memo[node] != 0:
                return memo[node] == 1

            memo[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            memo[node] = 1
            return True

        for i in range(n):
            if dfs(i):
                res.append(i)

        return res
