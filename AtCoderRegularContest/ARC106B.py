# https://atcoder.jp/contests/arc106/tasks/arc106_b

from collections import deque

N,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

root = [[] for i in range(N)]
for _ in range(M):
    c, d = (int(x) for x in input().split())
    root[c-1].append(d-1)
    root[d-1].append(c-1) 

check = [-1]*N

for j in range(N):
    if check[j] != -1:
        continue
    stack=deque([j])
    check[j] = j

    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i] = j
                stack.append(i)

memo = {}
for i in range(N):
    if check[i] in memo:
        memo[check[i]] += b[i]-a[i]
    else:
        memo[check[i]] = b[i]-a[i]

for key, val in memo.items():
    if val != 0:
        print('No')
        exit()
print('Yes')