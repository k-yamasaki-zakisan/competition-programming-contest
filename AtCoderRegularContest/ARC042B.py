# https://atcoder.jp/contests/arc042/tasks/arc042_b
# http://www.geisya.or.jp/~mwm48961/koukou/kyori04.htm
# https://manabitimes.jp/math/857

sX, sY = map(int, input().split())
N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 10**10
for i in range(N):
    x1, y1 = XY[i-1]
    x2, y2 = XY[i]
    by = -x2+x1
    ax = y2-y1
    c = (-y2+y1)*x1+(x2-x1)*y1
    tmp = abs(ax*sX+by*sY+c)/(ax**2+by**2)**0.5
    ans = min(ans, tmp)
print(ans)
