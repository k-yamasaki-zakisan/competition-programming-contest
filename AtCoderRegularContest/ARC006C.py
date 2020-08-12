#https://atcoder.jp/contests/arc006/tasks/arc006_3

import bisect

n=int(input())

w = []
for _ in range(n):
    a = int(input())
    w.append(a)

status = [w[0]]

for i in range(1,n):
    status.sort()
    p = bisect.bisect_left(status,w[i])
    if p == len(status):
        status.append(w[i])
    else:
        status[p] = w[i]
    #print(status)
print(len(status))
