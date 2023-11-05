from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


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
        parents_value = [[-1, -1] for _ in range(n)]
        dist_index = [[di, i] for i, di in enumerate(dist)]
        dist_index.sort()
        print(dist_index)


S = Solution()
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
values = [20, 10, 9, 7, 4, 3, 5]
print(S.maximumScoreAfterOperations(edges, values))
# 10
