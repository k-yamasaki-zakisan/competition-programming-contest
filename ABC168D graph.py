#https://atcoder.jp/contests/abc168/tasks/abc168_d

n,m = map(int,input().split())

root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 

stack=[0]
check = [-1]*n
check[0] = 0

while len(stack)>0:
    v = stack.pop(0)
    for i in root[v]:
        if check[i] == -1:
            check[i]=v+1
            stack.append(i)

if -1 in check:
    print('No')
else:
    print('Yes')
    for i in range(1,n):
        print(check[i])
