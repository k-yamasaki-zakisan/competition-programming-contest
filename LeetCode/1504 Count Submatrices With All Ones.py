class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        r, c = len(mat), len(mat[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j]:
                    dp[i][j] = 1 + (dp[i][j - 1] if j - 1 >= 0 else 0)
        for i in range(r):
            for j in range(c):
                mn = math.inf
                for k in range(i, -1, -1):
                    mn = min(mn, dp[k][j])
                    if mn == 0:
                        break
                    ans += mn
        return ans
