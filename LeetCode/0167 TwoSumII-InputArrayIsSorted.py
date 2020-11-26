# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Runtime: 64 ms, faster than 47.64% of Python3 online submissions for Two Sum II - Input array is sorted.
# Memory Usage: 14.6 MB, less than 14.57% of Python3 online submissions for Two Sum II - Input array is sorted.

class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        import bisect
        for i,num in enumerate(numbers):
            tmp = target-num
            target_i = bisect.bisect_right(numbers,tmp)
            if tmp == numbers[target_i-1]:
                return [i+1,target_i]