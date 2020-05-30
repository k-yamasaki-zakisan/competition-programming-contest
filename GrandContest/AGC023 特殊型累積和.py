#https://atcoder.jp/contests/agc023/tasks/agc023_a

import collections
n=int(input())

a = list(map(int,input().split()))

memo = [0]

for i in range(n):
    memo.append(memo[i]+a[i])

c = collections.Counter(memo)

score_sorted = sorted(c.items(), key=lambda x:-x[1])

ans = 0

for k,i in score_sorted:
    ans += i*(i-1)//2
print(ans)
