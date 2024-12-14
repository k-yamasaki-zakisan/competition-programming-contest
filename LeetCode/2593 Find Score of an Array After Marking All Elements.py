from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        used = set()
        ans = 0
        n = len(nums)
        sort_nums = sorted([[num, i] for i, num in enumerate(nums)])

        for num, i in sort_nums:
            if i in used:
                continue
            ans += num
            used.add(i)
            if 0 <= i - 1:
                used.add(i - 1)
            if i + 1 < n:
                used.add(i + 1)

        return ans
