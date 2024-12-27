from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_num = values[0]
        ans = 0
        for i in range(1, len(values)):
            ans = max(ans, max_num + values[i] - i)
            max_num = max(max_num, values[i] + i)
        return ans
