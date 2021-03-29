# https://atcoder.jp/contests/abc197/tasks/abc197_e

N = int(input())
XC = [list(map(int, input().split())) for _ in range(N)]
colors = [[] for _ in range(N)]
for x, c in XC:
    colors[c - 1].append(x)
for i in range(N):
    colors[i].sort()

ans = 0
now_l, now_r = 0, 0
cost_l, cost_r = 0, 0
for color in colors:
    if not color:
        continue
    next_l, next_r = color[0], color[-1]
    LEN = next_r - next_l
    next_cost_l = min(cost_l + abs(now_l-next_r),
                      cost_r + abs(now_r-next_r)) + LEN
    next_cost_r = min(cost_l + abs(now_l-next_l),
                      cost_r + abs(now_r-next_l)) + LEN
    now_l, now_r = next_l, next_r
    cost_l, cost_r = next_cost_l, next_cost_r
print(min(cost_l+abs(now_l), cost_r+abs(now_r)))
