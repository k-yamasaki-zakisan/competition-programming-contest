#https://atcoder.jp/contests/abc036/tasks/abc036_c

import copy
n=int(input())
ab = []
for _ in range(n):
    s=int(input())
    ab.append(s)
cd = copy.copy(ab)
ab = list(set(ab))

ab.sort()

ans = {}

for i in range(len(ab)):
    ans[ab[i]] = i

for i in cd:
    print(ans[i])
