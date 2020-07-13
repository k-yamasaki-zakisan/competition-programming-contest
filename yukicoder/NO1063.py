#https://yukicoder.me/problems/no/1063

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

c = collections.Counter(memo)

score_sorted = sorted(c.items(), key=lambda x:-x[0])

ans_a = 1
ans_b = 1

for idx, val in score_sorted:
    if 0 < val//2:
        ans_a *= idx**(val//2)
    if val%2==1:
        ans_b *= idx
print(ans_a, ans_b)
