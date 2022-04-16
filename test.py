import sys

sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

from math import gcd

N, K = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(N)]
if K == 1:
    print("Infinity")
    exit()

ans = set()
for i in range(N):
    x1, y1 = XY[i]
    for j in range(i + 1, N):
        x2, y2 = XY[j]
        dx, dy = (x2 - x1), (y2 - y1)
        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g
        cnt = 0
        tame = []
        for k in range(N):
            if k == i or k == j:
                cnt += 1
                tame.append(k)
                continue
            x3, y3 = XY[k]
            ddx, ddy = (x3 - x1), (y3 - y1)
            gg = gcd(ddx, ddy)
            ddx, ddy = ddx // gg, ddy // gg
            if (ddx == dx and ddy == dy) or (-ddx == dx and -ddy == dy):
                cnt += 1
                tame.append(k)
        if K <= cnt:
            ans.add((dx, dy, tuple(tame)))
            ans.add((-dx, -dy, tuple(tame)))
print(ans)
print(len(ans) // 2)
