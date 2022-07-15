# https://leetcode.com/problems/longest-turbulent-subarray/
# Runtime: 569 ms, faster than 81.76% of Python3 online submissions for Longest Turbulent Subarray.
# Memory Usage: 20.6 MB, less than 6.24% of Python3 online submissions for Longest Turbulent Subarray.

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        memo = []
        len_arr = len(arr)
        if len(set(arr)) == 1:
            return 1
        for i in range(len_arr - 1):
            if arr[i] < arr[i + 1]:
                memo.append("<")
            elif arr[i] > arr[i + 1]:
                memo.append(">")
            else:
                memo.append("=")
        ans = 1
        cnt = 1
        for i in range(1, len(memo)):
            if (memo[i - 1] == "<" and memo[i] == ">") or (
                memo[i - 1] == ">" and memo[i] == "<"
            ):
                cnt += 1
            else:
                ans = max(ans, cnt + 1)
                cnt = 1
        return max(ans, cnt + 1)
