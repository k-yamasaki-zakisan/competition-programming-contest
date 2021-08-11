# https://leetcode.com/problems/fair-candy-swap/
# Runtime: 356 ms, faster than 69.03% of Python3 online submissions for Fair Candy Swap.
# Memory Usage: 16.9 MB, less than 25.59% of Python3 online submissions for Fair Candy Swap.

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a = sum(aliceSizes)
        sum_b, memo_b = 0, set()
        for b in bobSizes:
            sum_b += b
            memo_b.add(b)
        sum_ab = sum_a+sum_b
        for a in aliceSizes:
            b = sum_ab//2-(sum_a-a)
            if b in memo_b:
                return [a, b]
