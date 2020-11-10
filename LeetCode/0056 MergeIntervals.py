# 
# Runtime: 76 ms, faster than 96.71% of Python3 online submissions for Merge Intervals.
# Memory Usage: 15.9 MB, less than 96.88% of Python3 online submissions for Merge Intervals.

class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort()
        if len(intervals):
            ans = [intervals[0]]
        else:
            return []
        for i in range(1,len(intervals)):
            tmp_a,tmp_b = intervals[i]
            if tmp_a <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], tmp_b)
            else:
                ans.append([tmp_a,tmp_b])
        return ans