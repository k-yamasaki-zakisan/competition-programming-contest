# https://atcoder.jp/contests/abc165/tasks/abc165_f

import bisect
N = int(input())
A = list(map(int,input().split()))
root = [[] for _ in range(N)]
for _ in range(N-1):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    root[u].append(v)
    root[v].append(u)

stack = [[0,-1]]
check = [False]*N
DP = [10**10]*N
L = [0]*N

while len(stack):
    x,a = stack.pop()
    if a == -1:
        check[x] = True
        i = bisect.bisect_left(DP, A[x])
        stack.append([i,DP[i]])
        DP[i] = A[x]
        L[x] = bisect.bisect_left(DP, 10**10)
        for y in root[x]:
            if not check[y]:
                stack.append([y,-1])
    else:
        DP[x] = a
print(*L, sep='\n')