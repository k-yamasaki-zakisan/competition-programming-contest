# https://atcoder.jp/contests/typical90/tasks/typical90_af

from collections import defaultdict
from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
XY = [list(map(int, input().split())) for _ in range(M)]
ng_list = defaultdict(list)
for x, y in XY:
    x -= 1
    y -= 1
    ng_list[x].append(y)
    ng_list[y].append(x)
ans = 10**10
for V in permutations(range(N)):
    ok_flag = True
    for i in range(1, len(V)):
        if V[i] in ng_list[V[i-1]]:
            ok_flag = False
            break
    if not ok_flag:
        continue
    tmp = 0
    for i, v in enumerate(V):
        tmp += A[v][i]
    ans = min(tmp, ans)
if ans == 10**10:
    print(-1)
else:
    print(ans)
