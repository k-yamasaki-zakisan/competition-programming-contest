#https://atcoder.jp/contests/cf17-final/tasks/cf17_final_b

import collections

s=input()

s=list(s)

c = collections.Counter(s)

score_sorted = sorted(c.items(), key=lambda x:-x[1])

val = []

for i, j in score_sorted:
    val.append(j)


if len(val) == 2:
    val.append(0)
elif len(val) == 1:
    val.append(0)
    val.append(0)
    
val.sort()

if 0<= val[2]-val[0] <=1:
    print('YES')
else:
    print('NO')
