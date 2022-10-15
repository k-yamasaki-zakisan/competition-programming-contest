# https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Runtime: 89 ms, faster than 96.05% of Python3 online submissions for Shortest Path with Alternating Colors.
# Memory Usage: 14 MB, less than 97.19% of Python3 online submissions for Shortest Path with Alternating Colors.

from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, N: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        from collections import deque

        ans = [-1] * N
        ans[0] = 0
        red_roots = [[] for _ in range(N)]
        blue_roots = [[] for _ in range(N)]
        for s, g in redEdges:
            red_roots[s].append(g)
        for s, g in blueEdges:
            blue_roots[s].append(g)
        stack = deque([[0, -1, 0]])
        visit_red, visit_blud = [False] * N, [False] * N
        visit_red[0] = visit_blud[0] = True
        while stack:
            now_p, color, cnt = stack.popleft()
            if color != 0:
                for next_p in red_roots[now_p]:
                    if not visit_red[next_p]:
                        stack.append([next_p, 0, cnt + 1])
                        visit_red[next_p] = True
                        if ans[next_p] == -1:
                            ans[next_p] = cnt + 1
            if color != 1:
                for next_p in blue_roots[now_p]:
                    if not visit_blud[next_p]:
                        stack.append([next_p, 1, cnt + 1])
                        visit_blud[next_p] = True
                        if ans[next_p] == -1:
                            ans[next_p] = cnt + 1
        return ans
