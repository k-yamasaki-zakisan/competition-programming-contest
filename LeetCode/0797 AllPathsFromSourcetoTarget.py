# https://leetcode.com/problems/all-paths-from-source-to-target/
# Runtime: 104 ms, faster than 48.55% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.7 MB, less than 44.64% of Python3 online submissions for All Paths From Source to Target.


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from copy import copy
        target_count = len(graph)
        visited = [False] * target_count
        visited[0] = True
        ans = []
        tmp = [0]

        def dfs(s):
            if s+1 == target_count:
                ans.append(copy(tmp))

            for i in graph[s]:
                if visited[i]:
                    continue

                visited[i] = True
                tmp.append(i)
                dfs(i)
                visited[i] = False
                tmp.pop()

        dfs(0)
        return ans
