from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        from collections import deque
        from collections import defaultdict

        n = len(coins)
        root = [[] for _ in range(n)]
        for s, g in edges:
            root[s].append(g)
            root[g].append(s)
        parents = [-1] * n
        visited = [-1] * n
        visited[0] = 0
        stack = deque([[0, 0]])
        ends = deque([])
        while len(stack):
            now, diff = stack.popleft()
            is_end = True
            for next in root[now]:
                if visited[next] == -1:
                    visited[next] = diff + 1
                    parents[next] = now
                    stack.append([next, diff + 1])
                    is_end = False
            if is_end:
                ends.append(now)
        method_1s = [-1] * n
        method_2s = [-1] * n
        parents_dict = defaultdict(list)
        for i in range(1, n):
            parents_dict[parents[i]].append(i)
        while len(ends):
            now = ends.popleft()
            method_1s[now] = coins[now] - k
            method_2s[now] = coins[now] // 2
        cands = [[diff, i] for i, diff in enumerate(visited)]
        cands.sort()
        print(cands)
        while len(cands):
            diff, now = cands.pop()
            tmp1, tmp2 = 0, 0
            for child in parents_dict[now]:
                tmp1 += max(method_1s[child], method_2s[child])
                tmp2 += (
                    method_2s[child] - (coins[child] // 2) + ((coins[child] // 2) // 2)
                )
            method_1s[now] = coins[now] - k + tmp1
            method_2s[now] = (coins[now] // 2) + tmp2
            if now == 0:
                break
        print(method_1s)
        print(method_2s)
        return max(method_1s[0], method_2s[0])


S = Solution()
edges = [[0, 1], [2, 0], [0, 3], [4, 2]]
coins = [7, 5, 0, 9, 3]
k = 4
print(S.maximumPoints(edges, coins, k))
# 10
