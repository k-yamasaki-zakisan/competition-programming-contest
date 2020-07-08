#https://atcoder.jp/contests/abc132/tasks/abc132_e

from collections import deque
 
N, M = map(int,input().split())
 
edges = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int,input().split())
    edges[u-1].append(v-1)
 
S, T = map(int,input().split())
S -= 1
T -= 1
 
visited = {}
q = deque()
q.append((S, 0))
d = -1
while q:
    s, c = q.popleft()
    if s in visited and (c % 3) in visited[s]:
        continue
    if s not in visited:
        visited[s] = set()
    visited[s].add(c % 3)
    for n in edges[s]:
        if n == T and c % 3 == 2:
            d = c + 1
            break
        q.append((n, c+1))
 
    if d % 3 == 0:
        break
 
if d == -1:
    print(-1)
else:
    print(d//3)
