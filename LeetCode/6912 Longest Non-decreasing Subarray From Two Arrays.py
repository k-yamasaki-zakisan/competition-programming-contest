from typing import List


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp1, dp2 = [1] * n, [1] * n
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = dp2[i - 1] + 1
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
        return max(max(dp1), max(dp2))
