# https://atcoder.jp/contests/abc219/tasks/abc219_d

INF = float('inf')

N = int(input())
X, Y = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
dp = [[[INF]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0] = 0
for i in range(N):
    a, b = AB[i]
    for j in range(X+1):
        for k in range(Y+1):
            if dp[i][j][k] != INF:
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                x, y = min(j+a, X), min(k+b, Y)
                dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][j][k]+1)

print(dp[N][X][Y] if dp[N][X][Y] != INF else -1)
