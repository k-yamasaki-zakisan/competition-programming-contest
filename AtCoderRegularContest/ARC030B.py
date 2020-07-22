#https://atcoder.jp/contests/arc030/tasks/arc030_2

import sys
import resource

sys.setrecursionlimit(1000000)


n,x = map(int,input().split())

h = list(map(int,input().split()))

root = [[] for i in range(n)]
for _ in range(n-1):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

root_memory = []

ans = []

visited = [False]*n
visited[x-1] = True

def dfs(s):
    global ans
    if h[s] == 1:
        ans = ans + root_memory
 
    for i in root[s]:
        if visited[i]:
            continue

        visited[i] = True
        root_memory.append(i)
        dfs(i)
        root_memory.pop(-1)
        visited[i] = False
    

dfs(x-1)

print(len(set(ans))*2)
