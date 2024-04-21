from heapq import heapify, heappop, heappush
from collections import deque
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        self.n = n
        ans = [False] * len(edges)
        cost = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b, w = edges[i]
            cost[a].append((b, w, i))
            cost[b].append((a, w, i))
        distance_from_0 = self.dij(cost, 0)
        q = deque([n - 1])
        while q:
            now = q.popleft()
            for go_to, w, i in cost[now]:
                if distance_from_0[now] - distance_from_0[go_to] == w:
                    ans[i] = True
                    q.append(go_to)
        return ans

    def dij(self, cost, start):
        d = [float("inf")] * self.n
        d[start] = 0

        q = [(d[start], start)]
        heapify(q)
        while q:
            du, u = heappop(q)
            if d[u] < du:
                continue
            for v, weight, _ in cost[u]:
                if du + weight < d[v]:
                    d[v] = du + weight
                    heappush(q, (d[v], v))
        return d
