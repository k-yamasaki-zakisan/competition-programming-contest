# https://leetcode.com/problems/next-greater-element-i/
# Runtime: 48 ms, faster than 71.17% of Python3 online submissions for Next Greater Element I.
# Memory Usage: 14.6 MB, less than 43.43% of Python3 online submissions for Next Greater Element I.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        nums2_point = defaultdict(int)
        for i, num2 in enumerate(nums2):
            nums2_point[num2] = i
        len_nums2 = len(nums2)
        ans = [-1]*len(nums1)
        for i, num1 in enumerate(nums1):
            if num1 in nums2_point:
                nums2_i = nums2_point[num1]
                for j in range(nums2_i+1, len_nums2):
                    if num1 < nums2[j]:
                        ans[i] = nums2[j]
                        break
        return ans
