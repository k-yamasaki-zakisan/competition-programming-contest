from typing import List


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        def check(mid, budget, i):
            for j in range(n):
                budget -= max(0, mid * composition[i][j] - stock[j]) * cost[j]
            return budget >= 0

        res = 0
        maxs = max(stock)
        for i in range(k):
            low, high = 0, budget + maxs
            while low < high:
                mid = (low + high + 1) // 2
                if check(mid, budget, i):
                    low = mid
                else:
                    high = mid - 1
            res = max(res, low)
        return res
