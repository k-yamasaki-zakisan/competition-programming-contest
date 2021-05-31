# https://atcoder.jp/contests/abc005/tasks/abc005_4

# 入力
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
P = [int(input()) for _ in range(Q)]
S = [[0]*(N+1) for _ in range(N+1)]

# ２次元累積和テーブル
for i in range(N):
    for j in range(N):
        S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + D[i][j]

# プレート範囲全探索
ans = [0]*(N*N+1)
for i in range(N):
    for j in range(N):
        for k in range(i+1, N+1):
            for l in range(j+1, N+1):
                now = (k-i)*(l-j)
                ans[now] = max(ans[now], S[k][l]-S[k][j]-S[i][l]+S[i][j])

# 最適化
for i in range(1, N*N+1):
    ans[i] = max(ans[i], ans[i-1])

# 出力
for p in P:
    print(ans[p])
