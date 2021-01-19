# https://leetcode.com/problems/teemo-attacking/
# Runtime: 236 ms, faster than 95.69% of Python3 online submissions for Teemo Attacking.
# Memory Usage: 15.5 MB, less than 82.96% of Python3 online submissions for Teemo Attacking.

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        timeSeries.sort()
        ans = 0
        head_time = timeSeries[0]
        for timeSerie in timeSeries:
            if timeSerie < head_time:
                ans += timeSerie+duration-head_time
            else:
                ans += duration
            head_time = timeSerie+duration
        return ans
