# https://leetcode.com/problems/two-sum/

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