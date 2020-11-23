# https://atcoder.jp/contests/abc184/tasks/abc184_d

A,B,C = map(int,input().split())
dp = [[[0]*101 for _ in range(101)] for _ in range(101)]

for i in range(99, A-1, -1):
    for j in range(99, B-1, -1):
        for k in range(99, C-1, -1):
            dp[i][j][k] += (dp[i+1][j][k]+1)*i/(i+j+k)
            dp[i][j][k] += (dp[i][j+1][k]+1)*j/(i+j+k)
            dp[i][j][k] += (dp[i][j][k+1]+1)*k/(i+j+k)
print(dp[A][B][C])