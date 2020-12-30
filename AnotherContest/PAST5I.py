# https://atcoder.jp/contests/past202012-open/tasks/past202012_i

from collections import deque

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
C = list(map(int, input().split()))
graph = [[]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if H[a] < H[b]:
        graph[a].append(b)
    else:
        graph[b].append(a)

visited = [-1]*N
stack = deque([])
for c in C:
    c -= 1
    visited[c] = 0
    stack.append(c)

while len(stack):
    q = stack.popleft()
    for v in graph[q]:
        if visited[v] == -1:
            visited[v] = visited[q]+1
            stack.append(v)
for step in visited:
    print(step)
