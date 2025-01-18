from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums2) % 2 == 1:
            for num1 in nums1:
                ans ^= num1
        if len(nums1) % 2 == 1:
            for num2 in nums2:
                ans ^= num2
        return ans
