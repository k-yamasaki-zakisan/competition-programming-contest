# https://leetcode.com/problems/summary-ranges/
# Runtime: 32 ms, faster than 33.68% of Python3 online submissions for Summary Ranges.
# Memory Usage: 14.4 MB, less than 11.38% of Python3 online submissions for Summary Ranges.

class Solution:
    def summaryRanges(self, nums: list) -> list:
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        tail = 0
        for i in range(len(nums)):
            if i == 0 and nums[i]+1 != nums[i+1]:
                ans.append(str(nums[i]))
                tail = 1
            elif i == len(nums)-1:
                if nums[i] != nums[i-1]+1:
                    ans.append(str(nums[i]))
                else:
                    ans.append(f'{nums[tail]}->{nums[i]}')
            else:
                if nums[i]+1 != nums[i+1]:
                    if tail == i:
                        ans.append(str(nums[i]))
                        tail = i+1
                    else:
                        ans.append(f'{nums[tail]}->{nums[i]}')
                        tail = i+1
        return ans
