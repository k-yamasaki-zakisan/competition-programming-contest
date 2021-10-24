# https://atcoder.jp/contests/abc224/tasks/abc224_d

from collections import deque
from copy import copy

M = int(input())
UV = [list(map(int, input().split())) for _ in range(M)]
P = list(map(int, input().split()))
root = [[] for _ in range(9)]
for u, v in UV:
    u, v = u-1, v-1
    root[u].append(v)
    root[v].append(u)
l = [8]*9
for i, p in enumerate(P):
    l[p-1] = i
start = l.index(8)
stack = deque([(start, l, 0)])
check = set()
check.add(''.join(map(str, l)))

while len(stack):
    now, status, cnt = stack.popleft()
    if status == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print(cnt)
        exit()
    for nxt in root[now]:
        status[now], status[nxt] = status[nxt], status[now]
        s = ''.join(map(str, status))
        if s not in check:
            check.add(s)
            stack.append((nxt, copy(status), cnt+1))
        status[now], status[nxt] = status[nxt], status[now]
print(-1)
