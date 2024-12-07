from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums) + 1
        while 1 < r - l:
            mid = (l + r) // 2
            tmp = 0
            for num in nums:
                if mid < num:
                    tmp += (num - 1) // mid
            if maxOperations < tmp:
                l = mid
            else:
                r = mid
        return l if sum([(num - 1) // l for num in nums]) <= maxOperations else r
