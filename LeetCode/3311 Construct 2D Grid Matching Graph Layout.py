from collections import deque
from typing import List


class Solution:
    def constructGridLayout(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        root = [[] for _ in range(n)]
        for a, b in edges:
            root[a].append(b)
            root[b].append(a)
        min_val = min([len(vals) for vals in root])
        starts = [i for i, vals in enumerate(root) if len(vals) == min_val]
        print(starts)
        start = starts[0]
        s_distance = [-1] * n
        s_distance[starts[0]] = 0
        cands = deque([starts[0]])
        while len(cands):
            now = cands.popleft()
            for next in root[now]:
                if s_distance[next] == -1:
                    cands.append(next)
                    s_distance[next] = s_distance[now] + 1
        if len(starts) == 2:
            ans = [[-1] * (max(s_distance) + 1)]
            for i in range(n):
                ans[0][s_distance[i]] = i
            return ans
        ends = [
            [diff, i] for i, diff in enumerate(s_distance) if i in starts and i != start
        ]
        ends.sort()
        print(ends)
        end = ends[0][-1]
        e_distance = [-1] * n
        e_distance[end] = 0
        cands = deque([end])
        while len(cands):
            now = cands.popleft()
            for next in root[now]:
                if e_distance[next] == -1:
                    cands.append(next)
                    e_distance[next] = e_distance[now] + 1
        tate = s_distance[ends[1][-1]]
        yoko = s_distance[ends[0][-1]]
        ans = [[-1] * (yoko + 1) for _ in range(tate + 1)]
        for i in range(n):
            diff = (s_distance[i] + e_distance[i] - yoko) // 2
            ans[diff][s_distance[i] - diff] = i
        return ans
