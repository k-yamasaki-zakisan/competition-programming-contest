# https://atcoder.jp/contests/abc185/tasks/abc185_e

N,M = map(int,input().split())
A = [-1]+list(map(int,input().split()))
B = [-1]+list(map(int,input().split()))
dp=[[0]*(M+10) for i in range(N+10)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i] == B[j]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+2)
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        dp[i][j] = max(dp[i][j], dp[i-1][j])
        dp[i][j] = max(dp[i][j], dp[i][j-1])
print(N+M-dp[N][M])