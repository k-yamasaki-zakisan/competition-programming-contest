#https://yukicoder.me/problems/no/977

from collections import deque

n = int(input())
 
root = [[] for i in range(n)]
for _ in range(n-1):
    a, b = (int(x) for x in input().split())
    root[b].append(a)
    root[a].append(b) 
 
stack=deque([0])
check = [-1]*n
check[0] = 1
 
while len(stack)>0:
    v = stack.popleft()
    for i in root[v]:
        if check[i] == -1:
            check[i]=check[v]+1
            stack.append(i)

if n == 2 or -1 not in check:
    print('Bob')
else:
    count_1 = check.count(-1)
    count_ren = 0
    for i in root:
        if len(i) < 2:
            count_ren += 1
    if count_1 < 2 and count_ren < 2:
        print('Bob')
    else:
        print('Alice')
