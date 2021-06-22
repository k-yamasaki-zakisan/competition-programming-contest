# https://atcoder.jp/contests/typical90/tasks/typical90_bt

import sys
sys.setrecursionlimit(10 ** 7)


def dps(y: int, x: int):
    global tmp, ans

    for i in range(4):
        ny, nx = y + DY[i], x + DX[i]
        if ([gy, gx] == [ny, nx]) and ([DY[i], DX[i]] != [-dy, -dx]):
            ans = max(ans, tmp)
        else:
            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] == 0 and C[ny][nx] != "#":
                tmp += 1
                d[ny][nx] = 1
                dps(ny, nx)
                tmp -= 1
                d[ny][nx] = 0


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
DY = [1, 0, -1, 0]
DX = [0, 1, 0, -1]

ans = -1
for gy in range(H):
    for gx in range(W):
        if C[gy][gx] == '.':
            for i in range(4):
                d = [[0] * W for _ in range(H)]
                d[gy][gx] = 1
                dy, dx = DY[i], DX[i]
                if 0 <= gy+dy < H and 0 <= gx+dx < W and C[gy+dy][gx+dx] != "#":
                    d[gy+dy][gx+dx] = 1
                    tmp = 2
                    dps(gy+dy, gx+dx)
print(ans)
