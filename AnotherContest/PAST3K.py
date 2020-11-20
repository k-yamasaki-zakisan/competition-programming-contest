# https://atcoder.jp/contests/past202005-open/tasks/past202005_k

N,Q = map(int,input().split())
FTX = [list(map(int,input().split())) for _ in range(Q)]
container = []
desk = []
for i in range(1,N+1):
    container.append(-1*i)
    desk.append(i)

for f,t,x in FTX:
    f,t,x = f-1,t-1,x-1
    tmp = desk[t]
    desk[t] = desk[f]
    desk[f] = container[x]
    container[x] = tmp

ans = [0]*N
for i in range(1,N+1):
    top = desk[i-1]-1
    if top<0:
        continue
    else:
        ans[top] = i
        while 0<container[top]:
            top = container[top]-1
            ans[top] = i
for a in ans:
    print(a)