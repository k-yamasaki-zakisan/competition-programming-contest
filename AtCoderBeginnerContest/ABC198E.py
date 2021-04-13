# https://atcoder.jp/contests/abc198/tasks/abc198_e

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
C = list(map(int, input().split()))
root = [[] for i in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    root[a-1].append(b-1)
    root[b-1].append(a-1)

tmp = [0]*(max(C)+1)
tmp[C[0]] += 1
visited = [False]*N
visited[0] = True
ans = [0]


def dfs(s):
    for r in root[s]:
        if visited[r]:
            continue
        tmp[C[r]] += 1
        if tmp[C[r]] == 1:
            ans.append(r)
        visited[r] = True
        dfs(r)
        tmp[C[r]] -= 1
        visited[r] = False


dfs(0)

ans.sort()
for a in ans:
    print(a+1)
