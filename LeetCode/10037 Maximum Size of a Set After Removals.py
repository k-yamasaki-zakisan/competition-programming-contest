from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        num1_kinds = set(nums1)
        num2_kind2 = set(nums2)
        if len(num1_kinds) <= len(nums1) // 2 and len(num2_kind2) <= len(nums2) // 2:
            return len(set(nums1 + nums2))
        else:
            if num1_kinds < num2_kind2:
                nums1, nums2 = nums2, nums1
                num1_kinds, num2_kind2 = num2_kind2, num1_kinds
            uniqu_nums1 = 0
            for n in num1_kinds:
                if n not in num2_kind2:
                    uniqu_nums1 += 1
            ans = 0
            amari = 0
            ans += min(len(nums1) // 2, uniqu_nums1)
            amari += max(0, len(nums1) // 2 - uniqu_nums1)
            same_cnt = len(num1_kinds) - uniqu_nums1
            uniqu_nums2 = len(num2_kind2) - same_cnt
            ans += min(len(nums2) // 2, uniqu_nums2)
            amari += max(0, len(nums2) // 2 - uniqu_nums2)
            ans += min(amari, same_cnt)
            return ans
