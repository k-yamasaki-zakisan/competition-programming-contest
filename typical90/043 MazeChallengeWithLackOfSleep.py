# https://atcoder.jp/contests/typical90/tasks/typical90_aq

from collections import deque

h, w = map(int, input().split())
sx, sy = map(lambda x: int(x)-1, input().split())
tx, ty = map(lambda x: int(x)-1, input().split())
matrix = [input() for _ in range(h)]

CNT = [[[10**10]*2 for j in range(w)] for i in range(h)]
CNT[sx][sy][0] = 0
CNT[sx][sy][1] = 0

DQ = deque([(0, sx, sy, 0), (0, sx, sy, 1)])
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while DQ:
    cnt, x, y, dir = DQ.popleft()

    if CNT[x][y][dir] < cnt:
        continue

    if x == tx and y == ty:
        print(cnt)
        exit()

    for turn in range(4):
        ndir = (dir+turn) % 4
        dx, dy = d[ndir]
        nx, ny = x+dx, y+dy

        if 0 <= nx <= h-1 and 0 <= ny <= w-1 and matrix[nx][ny] == ".":
            if turn % 2 == 0 and cnt < CNT[nx][ny][ndir % 2]:
                CNT[nx][ny][ndir % 2] = cnt
                DQ.appendleft((cnt, nx, ny, ndir % 2))

            elif cnt+1 < CNT[nx][ny][ndir % 2]:
                CNT[nx][ny][ndir % 2] = cnt + 1
                DQ.append((cnt+1, nx, ny, ndir % 2))
