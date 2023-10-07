from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_memo = set()
        point = 10**10
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num <= k and num not in nums_memo:
                nums_memo.add(num)
                point = i
        return len(nums) - point
