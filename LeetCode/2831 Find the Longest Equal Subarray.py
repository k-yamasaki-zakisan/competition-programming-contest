from typing import List
from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        points = defaultdict(list)
        for i, num in enumerate(nums):
            points[num].append(i)
        ans = 1
        for vals in points.values():
            if len(vals) == 1:
                continue
            head, tail = 0, 0
            while head < len(vals):
                if head == tail:
                    head += 1
                elif vals[head] - vals[tail] - (head - tail) <= k:
                    ans = max(ans, head - tail + 1)
                    head += 1
                else:
                    tail += 1
                # print(vals, tail, head)
        return ans
