# https://atcoder.jp/contests/abc187/tasks/abc187_e

from collections import deque

N = int(input())
AB = []
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    AB.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

Q = int(input())
TEX = [tuple(map(int, input().split())) for _ in range(Q)]

depth = [-1] * N
depth[0] = 0
queue = deque([0])
while len(queue):
    st = queue.popleft()
    for i in graph[st]:
        if depth[i] == -1:
            depth[i] = depth[st]+1
            queue.append(i)

s = [0]*N
for t, e, x in TEX:
    a, b = AB[e-1]
    if depth[a] > depth[b]:
        a, b = b, a
        if t == 1:
            t = 2
        else:
            t = 1
    if t == 1:
        s[0] += x
        s[b] -= x
    else:
        s[b] += x

queue = deque([0])
while len(queue):
    st = queue.popleft()
    for i in graph[st]:
        if depth[st] < depth[i]:
            s[i] += s[st]
            queue.append(i)

for ans in s:
    print(ans)
