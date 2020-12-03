# https://atcoder.jp/contests/cf16-final/tasks/codefestival_2016_final_c

from collections import deque

N,M = map(int,input().split())
KL = [list(map(int,input().split())) for _ in range(N)]
Graph = [[] for _ in range(2*10**6)]
for i, kl in enumerate(KL):
    i = 10**5+1+i
    l = kl[1:]
    for j in l:
        Graph[i].append(j)
        Graph[j].append(i)

check = [0]*(10**5+5+N)
stack = deque([10**5+1])
while len(stack):
    mover = stack.popleft()
    for m in Graph[mover]:
        if check[m] == 0:
            check[m] = 1
            stack.append(m)
if 0 in check[10**5+1:10**5+N+1]:
    print('NO')
else:
    print('YES')