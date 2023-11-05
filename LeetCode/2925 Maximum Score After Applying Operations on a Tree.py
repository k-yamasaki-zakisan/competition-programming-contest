from typing import List


class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        from collections import deque

        n = len(values)
        parents = [-1] * n
        roots = [[] for _ in range(n)]
        for s, g in edges:
            roots[s].append(g)
            roots[g].append(s)
        dist = [-1] * n
        dist[0] = 0
        stack = deque([0])
        while len(stack):
            now = stack.popleft()
            for next in roots[now]:
                if dist[next] == -1:
                    parents[next] = now
                    dist[next] = dist[now] + 1
                    stack.append(next)
        parents_value = [[0, values[i]] for i in range(n)]
        visited = [False] * n
        dist_index = [[di, i] for i, di in enumerate(dist)]
        dist_index.sort()
        while len(dist_index):
            _, now = dist_index.pop()
            p = parents[now]
            if visited[p]:
                continue
            visited[p] = True
            tmp_plus = 0
            tmp_lost = 0
            for child in roots[p]:
                if child == parents[p]:
                    continue
                tmp_plus += parents_value[child][0]
                tmp_lost += parents_value[child][1]
            if tmp_lost < values[p]:
                parents_value[p][0] = tmp_plus + values[p]
                parents_value[p][1] = tmp_lost
            else:
                parents_value[p][0] = tmp_plus + tmp_lost
                parents_value[p][1] = values[p]
            # print(parents_value)
        return parents_value[0][0]
