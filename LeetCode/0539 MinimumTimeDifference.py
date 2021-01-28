# https://leetcode.com/problems/minimum-time-difference/
# Runtime: 92 ms, faster than 19.31% of Python3 online submissions for Minimum Time Difference.
# Memory Usage: 17.2 MB, less than 9.78% of Python3 online submissions for Minimum Time Difference.

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        memo = []
        for time in timePoints:
            sec = int(time[:2])*60+int(time[-2:])
            memo.append(sec)
            memo.append(sec+24*60)
        memo.sort()
        ans = 10**10
        for i in range(1, len(memo)):
            ans = min(ans, memo[i]-memo[i-1])
        return ans
