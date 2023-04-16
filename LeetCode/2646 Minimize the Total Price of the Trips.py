from typing import List
from functools import lru_cache
from collections import deque


class Solution:
    def minimumTotalPrice(
        self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]
    ) -> int:
        INF = float("inf")

        root = [[] for _ in range(n)]
        for s, g in edges:
            root[s].append(g)
            root[g].append(s)
        repeats = [0] * n
        for s, g in trips:
            step_cnt = [-1] * n
            step_cnt[s] = 0
            stack = deque([s])
            while len(stack):
                now = stack.popleft()
                for next in root[now]:
                    if step_cnt[next] == -1:
                        step_cnt[next] = step_cnt[now] + 1
                        stack.append(next)
            stack = deque([g])
            repeats[g] += 1
            while len(stack):
                now = stack.popleft()
                for next in root[now]:
                    if step_cnt[next] == step_cnt[now] - 1:
                        repeats[next] += 1
                        stack.append(next)

        @lru_cache(None)
        def dfs(vertex: int, parent: int, parent_halved: bool):
            halved = INF if parent_halved else (price[vertex] * repeats[vertex]) // 2
            not_halved = price[vertex] * repeats[vertex]
            for next in root[vertex]:
                if next == parent:
                    continue
                if halved != INF:
                    halved += dfs(next, vertex, True)
                not_halved += dfs(next, vertex, False)
            return min(halved, not_halved)

        return dfs(0, -1, False)
