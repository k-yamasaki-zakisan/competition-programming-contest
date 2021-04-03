# https://leetcode.com/problems/shortest-distance-to-a-character/
# Runtime: 44 ms, faster than 38.81% of Python3 online submissions for Shortest Distance to a Character.
# Memory Usage: 14.3 MB, less than 84.88% of Python3 online submissions for Shortest Distance to a Character.

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        from collections import deque
        dp = [-1]*len(s)
        stack = deque([])
        for i, word in enumerate(s):
            if word == c:
                stack.append(i)
                dp[i] = 0

        while len(stack):
            now = stack.popleft()
            for i in [-1, 1]:
                next = now+i
                if 0 <= next < len(s) and dp[next] == -1:
                    dp[next] = dp[now]+1
                    stack.append(next)
        return dp
