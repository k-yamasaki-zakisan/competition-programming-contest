# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 68 ms, faster than 33.87% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 15 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import heapq
        remove_p = []
        max_p = sorted(prices)
        ans = 0
        for i in range(len(prices)-1):
            ans = max(ans, max_p[-1]-prices[i])
            heapq.heappush(remove_p,-1*prices[i])
            while len(remove_p) and max_p[-1] == -1*remove_p[0]:
                max_p.pop()
                heapq.heappop(remove_p)
        return ans


# Runtime: 60 ms, faster than 77.37% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.9 MB, less than 99.99% of Python3 online submissions for Best Time to Buy and Sell Stock.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1:
            return 0
        min_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            profit = max(profit, prices[i] - min_price)
        return profit