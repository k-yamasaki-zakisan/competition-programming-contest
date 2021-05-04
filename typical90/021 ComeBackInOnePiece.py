# https://atcoder.jp/contests/typical90/tasks/typical90_u

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(pos: int) -> None:
    used[pos] = True
    for v in G[pos]:
        if not used[v]:
            dfs(v)
        I.append(pos)


def dfs2(pos: int) -> None:
    global cnts
    used[pos] = True
    cnts += 1
    for i in H[pos]:
        if not used[i]:
            dfs2(i)


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
H = [[] for _ in range(N)]
used = [False]*N
I = []
for a, b in AB:
    a -= 1
    b -= 1
    G[a].append(b)
    H[b].append(a)

for i in range(N):
    if not used[i]:
        dfs(i)

ans = 0
print(I)
I = I[::-1]
print(I)
used = [False]*N
for i in I:
    if used[i]:
        continue
    cnts = 0
    dfs2(i)
    ans += cnts * (cnts - 1) // 2
print(ans)
