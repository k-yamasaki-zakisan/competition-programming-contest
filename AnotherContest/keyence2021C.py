# https://atcoder.jp/contests/keyence2021/tasks/keyence2021_c

H, W, K = map(int, input().split())
MOD = 998244353

dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][0] = pow(3, H*W-K, MOD)

m = [['N']*(W+1) for _ in range(H+1)]

for _ in range(K):
    h, w, c = map(str, input().split())
    h, w = int(h)-1, int(w)-1
    m[h][w] = c

i3 = pow(3, MOD-2, MOD)*2
for h in range(H):
    for w in range(W):
        if m[h][w] == 'R':
            dp[h][w+1] += dp[h][w]
        elif m[h][w] == 'D':
            dp[h+1][w] += dp[h][w]
        elif m[h][w] == 'X':
            dp[h][w+1] += dp[h][w]
            dp[h+1][w] += dp[h][w]
        elif m[h][w] == 'N':
            dp[h][w+1] += dp[h][w]*i3
            dp[h+1][w] += dp[h][w]*i3
        dp[h][w+1] %= MOD
        dp[h+1][w] %= MOD

print(dp[H-1][W-1])
