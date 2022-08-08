# https://leetcode.com/problems/max-consecutive-ones-iii/
# Runtime: 702 ms, faster than 81.76% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.7 MB, less than 59.64% of Python3 online submissions for Max Consecutive Ones III.

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = ans = cnt_k = last = 0
        for now in range(len(nums)):
            if nums[now] == 0:
                cnt_k += 1
            cnt += 1
            while k < cnt_k and last <= now:
                if nums[last] == 0:
                    cnt_k -= 1
                cnt -= 1
                last += 1
            ans = max(ans, cnt)
        return ans
