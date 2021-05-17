# https://atcoder.jp/contests/abc201/tasks/abc201_d

INF = float('inf')
H, W = map(int, input().split())
A = [input() for _ in range(H)]
dp = [[INF]*(W+1) for _ in range(H+1)]
dp[H-1][W-1] = 0
for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if H-1 == h and W-1 == w:
            continue
        if h < H-1:
            point_h = 1 if A[h+1][w] == '+' else -1
        if w < W-1:
            point_w = 1 if A[h][w+1] == '+' else -1
        if (h+w) % 2 == 0:
            if h < H-1 and w < W-1:
                dp[h][w] = max(dp[h+1][w]+point_h, dp[h][w+1]+point_w)
            elif w < W-1:
                dp[h][w] = dp[h][w+1]+point_w
            elif h < H-1:
                dp[h][w] = dp[h+1][w]+point_h
        else:
            if h < H-1 and w < W-1:
                dp[h][w] = min(dp[h+1][w]-point_h, dp[h][w+1]-point_w)
            elif w < W-1:
                dp[h][w] = dp[h][w+1]-point_w
            elif h < H-1:
                dp[h][w] = dp[h+1][w]-point_h
if 0 < dp[0][0]:
    print('Takahashi')
elif 0 == dp[0][0]:
    print('Draw')
elif dp[0][0] < 0:
    print('Aoki')
