from collections import defaultdict, deque
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        parent_cnt = defaultdict(int)
        root = [[] for _ in range(n)]
        for f, t in edges:
            parent_cnt[t] += 1
            root[f].append(t)
        candidates = deque([i for i in range(n) if parent_cnt[i] == 0])
        while len(candidates):
            now_point = candidates.popleft()
            for next_point in root[now_point]:
                ans[next_point] |= ans[now_point]
                ans[next_point].add(now_point)
                parent_cnt[next_point] -= 1
                if parent_cnt[next_point] == 0:
                    candidates.append(next_point)
        sorted_ans = []
        for a in ans:
            a_list = list(a)
            a_list.sort()
            sorted_ans.append(a_list)
        return sorted_ans
