#https://atcoder.jp/contests/arc032/tasks/arc032_2

from collections import deque
 
n,m = map(int,input().split())
 
root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 
 
check = [-1]*n

for k in range(n):
    if check[k] != -1:
        continue
    stack=deque([k])
    check[k] = k
    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i]=k
                stack.append(i)
ans = 0

color_join = {0:1}

for i in check:
    if i not in color_join:
        color_join[i] = 1
        ans += 1
print(ans)
