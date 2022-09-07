# https://leetcode.com/problems/flower-planting-with-no-adjacent/
# Runtime: 477 ms, faster than 87.79% of Python3 online submissions for Flower Planting With No Adjacent.
# Memory Usage: 21.3 MB, less than 75.90% of Python3 online submissions for Flower Planting With No Adjacent.

from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        from collections import deque

        root = [[] for _ in range(n)]
        for a, b in paths:
            a, b = a - 1, b - 1
            root[a].append(b)
            root[b].append(a)
        ans = [-1] * n
        for start in range(n):
            if ans[start] != -1:
                continue
            ans[start] = 1
            stack = deque([start])
            while stack:
                now = stack.popleft()
                for next in root[now]:
                    if ans[next] != -1:
                        continue
                    stack.append(next)
                    cad = set([1, 2, 3, 4])
                    for n in root[next]:
                        if ans[n] in cad:
                            cad.remove(ans[n])
                    cad = list(cad)
                    cad.sort()
                    ans[next] = cad[0]
        return ans
