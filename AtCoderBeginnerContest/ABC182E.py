# https://atcoder.jp/contests/abc182/tasks/abc182_e
# 軸を決めて,決めてない軸をスイング、明かりがついてるかを確認してメモ

H,W,N,M = map(int,input().split())
# 0: なし, 1: 明かりが届いている, 2: ブロック
Grid = [[0]*W for _ in range(H)]
for _ in range(N):
    a,b = map(int,input().split())
    Grid[a-1][b-1] = 1
for _ in range(M):
    c,d = map(int,input().split())
    Grid[c-1][d-1] = 2

ans = [[0] * W for _ in range(H)]
for h in range(H):
    cur = 0
    for w in range(W):
        if Grid[h][w] == 1:
            cur = 1
        elif Grid[h][w] == 2:
            cur = 0
        if ans[h][w] == 0:
            ans[h][w] = cur
    cur = 0
    for w in range(W-1,-1,-1):
        if Grid[h][w] == 1:
            cur = 1
        elif Grid[h][w] == 2:
            cur = 0
        if ans[h][w] == 0:
            ans[h][w] = cur
for w in range(W):
    cur = 0
    for h in range(H):
        if Grid[h][w] == 1:
            cur = 1
        elif Grid[h][w] == 2:
            cur = 0
        if ans[h][w] == 0:
            ans[h][w] = cur
    cur = 0
    for h in range(H-1,-1,-1):
        if Grid[h][w] == 1:
            cur = 1
        elif Grid[h][w] == 2:
            cur = 0
        if ans[h][w] == 0:
            ans[h][w] = cur
result = 0
for h in range(H):
    for w in range(W):
        if ans[h][w] == 1:
            result += 1
print(result)