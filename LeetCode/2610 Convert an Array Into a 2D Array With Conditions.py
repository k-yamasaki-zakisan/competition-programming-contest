from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count_nums = Counter(nums)
        max_count = max(count_nums.values())
        ans = [[] for _ in range(max_count)]
        for num, cnt in count_nums.items():
            for i in range(cnt):
                ans[i].append(num)
        return ans
