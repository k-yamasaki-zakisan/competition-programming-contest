from typing import List


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        from heapq import heappop, heappush

        N = len(nums)
        ans = float("inf")
        for i in range(N):
            tmp = x * i
            min_valus = []
            remove_value = []
            for j in range(i):
                heappush(min_valus, nums[j])
            for j in range(i, N + i):
                j_MOD = j % N
                heappush(min_valus, nums[j_MOD])
                tmp += min_valus[0]
                heappush(remove_value, nums[j - i])
                while (
                    len(min_valus)
                    and len(remove_value)
                    and min_valus[0] == remove_value[0]
                ):
                    heappop(min_valus)
                    heappop(remove_value)
            ans = min(ans, tmp)
        return ans
