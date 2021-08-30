# https://leetcode.com/problems/minimum-increment-to-make-array-unique/
# Runtime: 896 ms, faster than 29.60% of Python3 online submissions for Minimum Increment to Make Array Unique.
# Memory Usage: 33.2 MB, less than 6.78% of Python3 online submissions for Minimum Increment to Make Array Unique.

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        set_nums = set()
        base = -1
        for num in nums:
            if num in set_nums:
                ans += base-num+1
                num = base+1
            set_nums.add(num)
            base = num
        return ans
