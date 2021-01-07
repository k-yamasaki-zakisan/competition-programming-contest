# https://leetcode.com/problems/ugly-number-ii/
# Runtime: 224 ms, faster than 25.75% of Python3 online submissions for Ugly Number II.
# Memory Usage: 14.2 MB, less than 70.87% of Python3 online submissions for Ugly Number II.

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heappop, heappush
        cnt = 1
        ans_cnd = [1]
        while cnt < n:
            a = heappop(ans_cnd)
            while len(ans_cnd) and a == ans_cnd[0]:
                heappop(ans_cnd)
            for i in [2, 3, 5]:
                heappush(ans_cnd, a*i)
            cnt += 1
        return ans_cnd[0]


# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         n1, n2, n3 = 0, 0, 0
#         dp = [1] * n

#         for i in range(1, n):
#             dp[i] = min(dp[n1]*2, dp[n2]*3, dp[n3]*5)
#             if dp[i] == dp[n1]*2: n1 += 1
#             if dp[i] == dp[n2]*3: n2 += 1
#             if dp[i] == dp[n3]*5: n3 += 1
#         return dp[n-1]
