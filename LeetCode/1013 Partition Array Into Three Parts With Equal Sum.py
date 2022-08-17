# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Runtime: 445 ms, faster than 61.44% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
# Memory Usage: 21 MB, less than 82.55% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.

from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False
        base = sum_arr // 3
        tmp = cnt = 0
        for a in arr:
            tmp += a
            if tmp == base:
                cnt += 1
                tmp = 0
            if cnt == 3:
                return True
        return False
