# https://atcoder.jp/contests/typical90/tasks/typical90_ce

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
XY = [list(map(int, input().split())) for _ in range(Q)]
G = [[] for _ in range(N)]
for a, b in AB:
    a, b = a-1, b-1
    G[a].append(b)
    G[b].append(a)

base_len = int((2*M)**0.5)
large = []
for i, g in enumerate(G):
    if base_len <= len(g):
        large.append(i)

link = [[False]*len(large) for _ in range(N)]
for i in range(len(large)):
    for j in G[large[i]]:
        link[j][i] = True
    link[large[i]][i] = True

colors = [-1]*N
large_colors = [-1]*len(large)
for i, xy in enumerate(XY):
    x, y = xy
    x -= 1
    last = colors[x]
    for j in range(len(large)):
        if link[x][j]:
            last = max(last, large_colors[j])
    print(XY[last][1] if last != -1 else 1)
    if len(G[x]) < base_len:
        colors[x] = i
        for j in G[x]:
            colors[j] = i
    else:
        ptr = large.index(x)
        large_colors[ptr] = i
