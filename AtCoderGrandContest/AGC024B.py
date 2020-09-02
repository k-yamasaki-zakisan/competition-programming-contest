#https://atcoder.jp/contests/agc024/tasks/agc024_b

N = int(input())
P = [int(input()) for _ in range(N)]
dp = [0]*N
for i in range(N):
    if P[i] == 1:
        dp[P[i]-1] = 1
    else:
        if dp[P[i]-2] == 0:
            dp[P[i]-1] = 1
        else:
            dp[P[i]-1] = dp[P[i]-2]+1
print(N-max(dp))
