# https://atcoder.jp/contests/indeednow-qualb/tasks/indeednow_2015_qualc_3

import heapq

N = int(input())

root = [[] for i in range(N)]
for _ in range(N-1):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 

ans = []
stack=[]
heapq.heappush(stack,0)
check = [-1]*N
check[0] = 1

while len(stack)>0:
    v = heapq.heappop(stack)
    ans.append(v+1)
    for i in root[v]:
        if check[i] == -1:
            check[i]=1
            heapq.heappush(stack,i)
print(*ans)