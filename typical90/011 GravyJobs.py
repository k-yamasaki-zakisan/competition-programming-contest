# https://atcoder.jp/contests/typical90/tasks/typical90_k

N = int(input())
DCS = [list(map(int, input().split())) for _ in range(N)]
DCS = sorted(DCS, key=lambda x: x[0])
DCS = [[0, 0, 0]] + DCS
dp = [[0]*(5001) for _ in range(5001)]
for i in range(N):
    nd, nc, ns = DCS[i+1]
    for j in range(5001):
        # 仕事 i + 1 をやらない場合
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        # 仕事 i + 1 をやる場合
        if j + nc <= nd:
            dp[i+1][j+nc] = max(dp[i+1][j+nc], dp[i][j]+ns)
ans = 0
for i in range(5001):
    ans = max(ans, dp[N][i])
print(ans)
