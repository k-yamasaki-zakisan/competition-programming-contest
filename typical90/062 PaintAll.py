# https://atcoder.jp/contests/typical90/tasks/typical90_bj

from collections import deque

N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
G = [[] for _ in range(10**5+1)]
usable = [False]*(10**5+1)

Q = deque([])
for i in range(N):
    a, b = AB[i]
    G[a].append(i+1)
    G[b].append(i+1)
    if a == i+1 or b == i+1:
        usable[i+1] = True
        Q.append(i+1)

vec = []
while len(Q):
    pos = Q.popleft()
    vec.append(pos)
    for i in G[pos]:
        if usable[i]:
            continue
        usable[i] = True
        Q.append(i)

vec = vec[::-1]
if len(vec) != N:
    print(-1)
else:
    for v in vec:
        print(v)
