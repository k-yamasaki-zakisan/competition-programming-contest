# https://atcoder.jp/contests/abc113/tasks/abc113_c

# case1 座標圧縮
from heapq import heappop, heappush
from collections import defaultdict
n, m = map(int, input().split())
py = []
p_y = [[] for i in range(n)]
for _ in range(m):
    p, y = map(int, input().split())
    py.append((p, y))
    p_y[p-1].append(y)
ans = {}
for i, tmp in enumerate(p_y):
    cnt = 1
    p_y[i] = tmp.sort()
    for j, jj in enumerate(tmp):

        ans[(i+1, jj)] = str(i+1).zfill(6) + str(j+1).zfill(6)


for i, tmp in enumerate(py):
    print(ans[tmp])


# case2 heapq

N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]
ans = ['']*M
memo = defaultdict(list)
for i, py in enumerate(PY):
    p, y = py
    heappush(memo[p], (y, i))
for key, val_list in memo.items():
    count = 0
    while len(val_list):
        y, ansi = heappop(val_list)
        ans[ansi] = str(key).zfill(6)+str(count+1).zfill(6)
        count += 1
for a in ans:
    print(a)
