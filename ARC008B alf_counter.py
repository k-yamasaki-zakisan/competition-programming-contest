#https://atcoder.jp/contests/arc008/tasks/arc008_2

import collections

n,m = map(int,input().split())

name=list(input())

kit=list(input())

c = collections.Counter(name)

name_count = sorted(c.items(), key=lambda x:-x[1])

memo = [0]*26

alf = [chr(ord('A') + i) for i in range(26)]

for i in range(m):
    alf_num = alf.index(kit[i])
    memo[alf_num] += 1

ans = -1

for i , j in name_count:
    a=alf.index(i)
    if memo[a] == 0:
        print(-1)
        exit()

    if j%memo[a] == 0:
        kazu = j//memo[a]
    else:
        kazu = 1 + j//memo[a]

    ans = max(ans,kazu,1)
print(ans)
