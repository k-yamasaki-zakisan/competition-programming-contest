#https://atcoder.jp/contests/abc127/tasks/abc127_d

import heapq

n,m = map(int,input().split())

a = list(map(int,input().split()))
bc = []
for _ in range(m):
    b, c = (int(x) for x in input().split())
    bc.append([b, c])
bc = sorted(bc, key=lambda x: -x[1])

heapq.heapify(a)

for i in range(m):
    count = 0
    if bc[i][1] < a[0]:
        break
    while a[0] < bc[i][1] and count < bc[i][0]:
        heapq.heappop(a)
        heapq.heappush(a,bc[i][1])
        count += 1
print(sum(a))
