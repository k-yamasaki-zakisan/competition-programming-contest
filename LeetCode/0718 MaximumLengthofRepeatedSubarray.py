# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# Runtime: 2556 ms, faster than 89.64% of Python3 online submissions for Maximum Length of Repeated Subarray.
# Memory Usage: 39.4 MB, less than 62.51% of Python3 online submissions for Maximum Length of Repeated Subarray.

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_A, len_B = len(A), len(B)
        dp = [[0]*(len_B+1) for _ in range(len_A+1)]
        for i in range(len_A-1, -1, -1):
            for j in range(len_B-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]+1
        return max(max(row) for row in dp)
