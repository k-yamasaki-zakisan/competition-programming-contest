# https://atcoder.jp/contests/abc248/tasks/abc248_e

from math import gcd
from collections import defaultdict

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
if K == 1:
    print("Infinity")
    exit()

ans = set()
for i in range(N):
    x1, y1 = XY[i]
    memo = defaultdict(int)
    memo_p = defaultdict(list)
    for j in range(N):
        if i == j:
            continue
        x2, y2 = XY[j]
        dx, dy = (x2 - x1), (y2 - y1)
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        memo[(dx, dy)] += 1
        memo[(-dx, -dy)] += 1
        memo_p[(dx, dy)].append(j)
        memo_p[(-dx, -dy)].append(j)
    for key in memo.keys():
        ddx, ddy = key
        if K <= memo[key] + 1:
            ans.add((ddx, ddy, memo_p[key][-1]))
print(len(ans) // 4)
