from typing import List
from collections import Counter


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_num = max(max(nums1), max(nums2)) + 10
        memo = [0] * max_num
        nums2_cnts = Counter(nums2)
        for num2, cnt in nums2_cnts.items():
            origin = num2 * k
            tmp = origin
            while tmp < max_num:
                memo[tmp] += cnt
                tmp += origin
        ans = 0
        for num1 in nums1:
            ans += memo[num1]
        return ans
