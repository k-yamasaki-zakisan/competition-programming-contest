#https://atcoder.jp/contests/abc169/tasks/abc169_d

def prime(p):
    memo = []
    for i in range(2,(int(p**0.5)+1)):
        while p%i==0:
            p //= i
            memo.append(i)
    if p != 1:
        memo.append(p)
    return memo

import collections

n=int(input())

memo = prime(n)

memo = collections.Counter(memo)

memo = sorted(memo.items(), key=lambda x:-x[1])

ans = 0

for sosu, count in memo:
  kosu = 1
  while 0 <= count-kosu:
    count -= kosu
    ans += 1
    kosu += 1
print(ans)
