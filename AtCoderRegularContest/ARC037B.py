#https://atcoder.jp/contests/arc037/tasks/arc037_b

from collections import deque
 
n,m = map(int,input().split())
 
root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 

check = [-1]*n

ans = 0

for j in range(n):
    if check[j] != -1:
        continue
    ans += 1
    stack=deque([j])
    check[j] = j
    flag = False
    while len(stack)>0:
        v = stack.popleft()
        for i in root[v]:
            if check[i] == -1:
                check[i]=v+1
                stack.append(i)
                search_index=root[i].index(v)
                root[i].pop(search_index)
            else:
                flag = True
    if flag:
        ans -= 1
print(ans)
