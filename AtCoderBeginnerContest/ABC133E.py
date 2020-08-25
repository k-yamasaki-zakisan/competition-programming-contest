#https://atcoder.jp/contests/abc133/tasks/abc133_e

from collections import deque

N,K = map(int,input().split())
mod = 1000000007
root = [[] for i in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    root[a-1].append(b-1)
    root[b-1].append(a-1)

stack=deque([[0,K]])
check = [True]*N
check[0] = False
ans = 1
while len(stack):
    u,k = stack.popleft()
    ans = (ans*k)%mod
    if u == 0:
        k_next = K-1
    else:
        k_next = K-2
    for v in root[u]:
        if check[v]:
            check[v] = False
            stack.append([v,k_next])
            k_next -= 1
    #print(ans, k_next)
print(ans)
