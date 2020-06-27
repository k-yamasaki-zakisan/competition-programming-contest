#https://atcoder.jp/contests/abc160/tasks/abc160_d

from collections import deque
 
n,x,y = map(int,input().split())
 
root = [[] for i in range(n)]
for i in range(1,n):
    root[i-1].append(i)
    root[i].append(i-1)

root[x-1].append(y-1)
root[y-1].append(x-1)

reselt = [0]*(n-1)

for i in range(n):
    stack=deque([i])
    check = [-1]*n
    check[i] = 0
 
    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i] = check[v]+1
                reselt[check[i]-1] += 1
                stack.append(i)

for i in reselt:
    print(i//2)
