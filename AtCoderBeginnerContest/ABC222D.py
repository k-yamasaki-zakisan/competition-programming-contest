# https://atcoder.jp/contests/abc222/tasks/abc222_d

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_v = max(B)
dp = [[0]*(max_v+10) for _ in range(N+1)]
for j in range(A[0], B[0]+1):
    dp[0][j] = 1

for i in range(1, N):
    a, b = A[i], B[i]
    tmp = 0
    for j in range(b+1):
        tmp += dp[i-1][j]
        if a <= j <= b:
            dp[i][j] = tmp % MOD
print(sum(dp[N-1]) % MOD)
