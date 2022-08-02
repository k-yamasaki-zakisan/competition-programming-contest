# https://leetcode.com/problems/find-the-town-judge/
# Runtime: 8723 ms, faster than 5.09% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19 MB, less than 65.83% of Python3 online submissions for Find the Town Judge.

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        for i in range(n):
            flag = True
            cnt = 0
            for a, b in trust:
                if i + 1 == a:
                    flag = False
                if i + 1 == b:
                    cnt += 1
            if flag and cnt == n - 1:
                return i + 1
        return -1
