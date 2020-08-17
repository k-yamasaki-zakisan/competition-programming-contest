#https://atcoder.jp/contests/dp/tasks/dp_h

mod = 1000000007

H,W = map(int,input().split())
root = []
for _ in range(H):
    s = list(input())
    root.append(s)

dp = [[0]*(W+1) for _ in range(H+1)]
dp[0][0] = 1
for h in range(H):
    for w in range(W):
        if root[h][w] == '#':
            continue
        if (h != 0 or w != 0):
            dp[h][w] = (dp[h-1][w] + dp[h][w-1])%mod

print(dp[H-1][W-1])
