# https://leetcode.com/problems/next-greater-element-ii/
# Runtime: 3404 ms, faster than 11.82% of Python3 online submissions for Next Greater Element II.
# Memory Usage: 15.8 MB, less than 66.88% of Python3 online submissions for Next Greater Element II.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        nums = nums*2
        for i in range(len(ans)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    ans[i] = nums[j]
                    break
        return ans
