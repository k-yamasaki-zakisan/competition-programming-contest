from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        from collections import defaultdict

        pre_memo = defaultdict(list)
        require = defaultdict(int)
        for a, b in prerequisites:
            pre_memo[b].append(a)
            require[a] += 1
        initial_value = []
        for i in range(numCourses):
            if require[i] == 0:
                initial_value.append(i)
        stack = deque(initial_value.copy())
        ans = initial_value.copy()
        used = set(initial_value)
        while len(stack):
            now = stack.popleft()
            for next in pre_memo[now]:
                if next in used:
                    continue
                used.add(next)
                ans.append(next)
                stack.append(next)
        return ans


S = Solution()
numCourses = 3
prerequisites = [[0, 1], [0, 2], [1, 2]]
print(S.findOrder(numCourses, prerequisites))
# [2,1,0]
