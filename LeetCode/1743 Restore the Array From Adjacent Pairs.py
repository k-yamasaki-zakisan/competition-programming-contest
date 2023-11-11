from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        from collections import defaultdict, Counter, deque

        root = defaultdict(set)
        visited = defaultdict(bool)
        tmp = []
        for s, g in adjacentPairs:
            tmp.append(s)
            tmp.append(g)
            root[s].add(g)
            root[g].add(s)
            visited[s] = False
            visited[g] = False
        count_tmp = Counter(tmp)
        stack = deque()
        ans = []
        for key, val in count_tmp.items():
            if val == 1:
                visited[key] = True
                stack.append(key)
                ans.append(key)
                break
        while len(stack):
            now = stack.popleft()
            for next in root[now]:
                if not visited[next]:
                    visited[next] = True
                    stack.append(next)
                    ans.append(next)
        return ans
