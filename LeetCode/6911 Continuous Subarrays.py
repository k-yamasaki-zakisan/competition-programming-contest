from typing import List
from heapq import heappop, heappush


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans, left = 0, 0
        n = len(nums)
        max_heap, min_heap = [], []
        max_expired, min_expired = [], []

        for right in range(n):
            heappush(min_heap, nums[right])
            heappush(max_heap, -nums[right])
            while -max_heap[0] - min_heap[0] > 2:
                heappush(min_expired, nums[left])
                heappush(max_expired, -nums[left])
                left += 1
                while len(max_expired) and max_expired[0] == max_heap[0]:
                    heappop(max_expired)
                    heappop(max_heap)
                while len(min_expired) and min_expired[0] == min_heap[0]:
                    heappop(min_expired)
                    heappop(min_heap)

            ans += right - left + 1

        return ans
