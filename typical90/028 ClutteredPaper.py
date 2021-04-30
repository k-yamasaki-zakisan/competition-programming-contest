# https://atcoder.jp/contests/typical90/tasks/typical90_ab

from collections import defaultdict
num_dic = defaultdict(int)

N = int(input())
LRXY = [list(map(int, input().split())) for _ in range(N)]
map_x = [[0]*1009 for _ in range(1009)]
map_y = [[0]*1009 for _ in range(1009)]
for lx, ly, rx, ry in LRXY:
    map_x[ly][lx] += 1
    map_x[ly][rx] -= 1
    map_y[ry][lx] -= 1
    map_y[ry][rx] += 1
dpx = [[0]*1009 for _ in range(1009)]
dpy = [[0]*1009 for _ in range(1009)]
dp = [[0]*1009 for _ in range(1009)]
for h in range(1005):
    for w in range(1005):
        dpx[h][w] = map_x[h][w] + dpx[h][w-1]
        dpy[h][w] = map_y[h][w] + dpy[h][w-1]
for w in range(1005):
    for h in range(1, 1005):
        dpx[h][w] += dpx[h-1][w]
        dpy[h][w] += dpy[h-1][w]


for h in range(1001):
    for w in range(1001):
        num = dpx[h][w]+dpy[h][w]
        num_dic[num] += 1

for i in range(1, N+1):
    print(num_dic[i])
