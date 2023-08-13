from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        from collections import defaultdict

        pre_memo = defaultdict(list)
        use_cnt = defaultdict(int)
        for a, b in prerequisites:
            pre_memo[b].append(a)
            use_cnt[a] += 1
        stack = deque()
        ans = []
        for i in range(numCourses):
            if use_cnt[i] == 0:
                stack.append(i)
                ans.append(i)
        while len(stack):
            now = stack.popleft()
            for next in pre_memo[now]:
                use_cnt[next] -= 1
                if use_cnt[next]:
                    continue
                ans.append(next)
                stack.append(next)
        return ans if len(ans) == numCourses else []
