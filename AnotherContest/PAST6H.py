# https://atcoder.jp/contests/past202104-open/tasks/past202104_h

# ABC175の類題
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
dp = [[[0]*(W+1) for _ in range(H+1)] for _ in range(H+W)]
for y in range(H):
    for x in range(W):
        for i in range(y+x+1):
            position = dp[i][y][x]
            if y+1 <= H:
                dp[i][y+1][x] = max(dp[i][y+1][x], position)
                dp[i+1][y+1][x] = max(dp[i+1][y+1][x], position+A[y][x])
            if x+1 <= W:
                dp[i][y][x+1] = max(dp[i][y][x+1], position)
                dp[i+1][y][x+1] = max(dp[i+1][y][x+1], position+A[y][x])
for i in range(1, H+W):
    print(dp[i][H][W-1])
