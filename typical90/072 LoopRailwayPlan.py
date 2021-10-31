# https://atcoder.jp/contests/typical90/tasks/typical90_bt

import sys
sys.setrecursionlimit(10 ** 7)


def dps(n_h, n_w, cnt):
    global ans
    for y, x in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        j_h, j_w = n_h+y, n_w+x
        if j_h == h and j_w == w:
            ans = max(ans, cnt+1)
            continue
        if 0 <= j_h < H and 0 <= j_w < W and C[j_h][j_w] == '.' and check[j_h][j_w] == False:
            check[j_h][j_w] = True
            dps(j_h, j_w, cnt+1)
            check[j_h][j_w] = False


H, W = map(int, input().split())
C = [input() for _ in range(H)]
ans = -1
for h in range(H):
    for w in range(W):
        if C[h][w] == '.':
            check = [[False]*W for _ in range(H)]
            check[h][w] = True
            dps(h, w, 0)
if 2 < ans:
    print(ans)
else:
    print(-1)
