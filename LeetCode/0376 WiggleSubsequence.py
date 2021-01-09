# https://leetcode.com/problems/wiggle-subsequence/
# Runtime: 52 ms, faster than 22.12% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.2 MB, less than 65.36% of Python3 online submissions for Wiggle Subsequence.

class Solution:
    def wiggleMaxLength(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        nums_new = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums_new.append(nums[i])
        if len(nums_new) < 3:
            return len(nums_new)
        ans = 2
        up_flag = nums_new[0] < nums_new[1]
        for i in range(2, len(nums_new)):
            print(nums_new[i], i, ans)
            if up_flag:
                if nums_new[i-1] > nums_new[i]:
                    ans += 1
                    up_flag = not up_flag
            else:
                if nums_new[i-1] < nums_new[i]:
                    ans += 1
                    up_flag = not up_flag
        return ans
