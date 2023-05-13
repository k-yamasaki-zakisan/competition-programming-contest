from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def minimumCost(
        self, start: List[int], target: List[int], specialRoads: List[List[int]]
    ) -> int:
        points = {}
        points[tuple(start)] = 0
        points[tuple(target)] = 1
        p = 2
        for x1, y1, x2, y2, cost in specialRoads:
            if (x1, y1) not in points:
                points[(x1, y1)] = p
                p += 1
            if (x2, y2) not in points:
                points[(x2, y2)] = p
                p += 1
        costs = [[] for _ in range(len(points))]
        costs[points[tuple(start)]].append(
            [
                points[tuple(target)],
                abs(start[0] - target[0]) + abs(start[1] - target[1]),
            ]
        )
        for x1, y1, x2, y2, cost in specialRoads:
            costs[points[tuple(start)]].append(
                [points[(x1, y1)], abs(start[0] - x1) + abs(start[1] - y1)]
            )
            costs[points[(x1, y1)]].append([points[(x2, y2)], cost])
            costs[points[tuple(target)]].append(
                [points[(x2, y2)], abs(target[0] - x2) + abs(target[1] - y2)]
            )
        for i in range(len(specialRoads) - 1):
            x11, y11, x21, y21, cost2 = specialRoads[i]
            for j in range(i + 1, len(specialRoads)):
                x12, y12, x22, y22, cost2 = specialRoads[j]
                costs[points[(x21, y21)]].append(
                    [points[(x12, y12)], abs(x21 - x12) + abs(y21 - y12)]
                )
        result = self.dij(costs, points[tuple(start)])
        print(result)
        return result[points[tuple(target)]]

    def dij(self, cost, start):
        import heapq

        d = [float("inf")] * len(cost)  # 最短距離
        d[start] = 0

        q = [(d[start], start)]  # min-heap, (距離, 頂点)
        heapq.heapify(q)
        while q:
            du, u = heapq.heappop(q)  # 最短距離とその頂点
            if d[u] < du:
                continue
            for v, weight in cost[u]:
                if du + weight < d[v]:
                    d[v] = du + weight
                    heapq.heappush(q, (d[v], v))
        return d


S = Solution()

start = [1, 1]
target = [5, 10]
specialRoads = [[3, 4, 5, 2, 5], [4, 5, 3, 8, 3], [3, 2, 5, 3, 1]]
print(S.minimumCost(start, target, specialRoads))
