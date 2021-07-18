# https://atcoder.jp/contests/abc210/tasks/abc210_d

INF = float('inf')

H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [a.copy() for a in A]
ans = INF
for h in range(H):
    for w in range(W):
        if h:
            ans = min(ans, dp[h-1][w] + C + A[h][w])
            dp[h][w] = min(dp[h][w], dp[h-1][w] + C)
        if w:
            ans = min(ans, dp[h][w-1] + C + A[h][w])
            dp[h][w] = min(dp[h][w], dp[h][w-1] + C)

A = [a[::-1] for a in A]
dp = [a.copy() for a in A]
for h in range(H):
    for w in range(W):
        if h:
            ans = min(ans, dp[h-1][w] + C + A[h][w])
            dp[h][w] = min(dp[h][w], dp[h-1][w] + C)
        if w:
            ans = min(ans, dp[h][w-1] + C + A[h][w])
            dp[h][w] = min(dp[h][w], dp[h][w-1] + C)
print(ans)
