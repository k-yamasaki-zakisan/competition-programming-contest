# https://atcoder.jp/contests/typical90/tasks/typical90_z

from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N-1)]
root = [[] for i in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    root[b].append(a)
    root[a].append(b)


def bps(start: int) -> list:
    stack = deque([start])
    check = [-1]*N
    check[start] = 0
    while len(stack) > 0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i] = check[v]+1
                stack.append(i)
    return check


tmp_colors = bps(0)
max_index = tmp_colors.index(max(tmp_colors))
colors = bps(max_index)
ans1, ans2 = [], []
for i, color in enumerate(colors):
    if color % 2 == 1:
        ans1.append(i+1)
    else:
        ans2.append(i+1)
if len(ans1) < len(ans2):
    print(*ans2[:N//2])
else:
    print(*ans1[:N//2])
