#https://atcoder.jp/contests/abc134/tasks/abc134_e

import bisect
n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
color = [a[n-1]]
for i in range(n-2,-1,-1):
    if a[i]>=color[-1]:
        color.append(a[i])
    else:
        x = bisect.bisect_right(color,a[i])
        color[x] = a[i]
print(len(color))
