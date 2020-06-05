#https://atcoder.jp/contests/past202004-open/tasks/past202004_b

import collections

s=list(input())

c = collections.Counter(s)

score_sorted = sorted(c.items(), key=lambda x:-x[1])

print(score_sorted[0][0])
