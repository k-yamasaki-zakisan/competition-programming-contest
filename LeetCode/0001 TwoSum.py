# https://leetcode.com/problems/two-sum/
# Runtime: 44 ms, faster than 91.36% of Python3 online submissions for Two Sum.
# Memory Usage: 15.5 MB, less than 16.89% of Python3 online submissions for Two Sum.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_cdd = {}
        for i,num in enumerate(nums):
            if num in ans_cdd:
                return [ans_cdd[num],i]
            else:
                cdd = target-num
                ans_cdd[cdd] = i
        return -1