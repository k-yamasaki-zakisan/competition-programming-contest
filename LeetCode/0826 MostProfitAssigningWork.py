# https://leetcode.com/problems/most-profit-assigning-work/
# Runtime: 760 ms, faster than 5.23% of Python3 online submissions for Most Profit Assigning Work.
# Memory Usage: 17.3 MB, less than 21.14% of Python3 online submissions for Most Profit Assigning Work.


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        points = [0]*(1+max(max(difficulty), max(worker)))
        for i in range(len(difficulty)):
            diff, benefit = difficulty[i], profit[i]
            points[diff] = max(points[diff], benefit)
        for i in range(1, len(points)):
            points[i] = max(points[i], points[i-1])
        ans = 0
        for w in worker:
            ans += points[w]
        return ans
