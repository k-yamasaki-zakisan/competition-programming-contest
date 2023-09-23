from typing import List
from array import array
from bisect import bisect


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        len_nums = len(nums)
        sep = array("I", [])
        ans = float(inf)
        for i in range(len_nums - x - 1, -1, -1):
            add_p = bisect(sep, nums[i + x])
            sep.insert(add_p, nums[i + x])
            p = bisect(sep, nums[i])
            if p < len(sep):
                ans = min(ans, abs(sep[p] - nums[i]))
            if 0 < p:
                ans = min(ans, abs(sep[p - 1] - nums[i]))
        return ans
