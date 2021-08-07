# https://leetcode.com/problems/koko-eating-bananas/
# Runtime: 472 ms, faster than 66.06% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15.5 MB, less than 62.24% of Python3 online submissions for Koko Eating Bananas.

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high, low = 10**9+10, 0
        while 1<high-low:
            mid = (high+low)//2
            tmp = 0
            for pile in piles:
                tmp += pile//mid+1 if pile%mid else pile//mid
            if h<tmp:
                low = mid
            else:
                high = mid
        return high