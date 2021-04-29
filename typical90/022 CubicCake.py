# https://atcoder.jp/contests/typical90/tasks/typical90_v

from math import gcd

A, B, C = map(int, input().split())
tmp = gcd(A, B)
gcd_abc = gcd(tmp, C)
ans = 0
if A != gcd_abc:
    ans += A//gcd_abc-1
if B != gcd_abc:
    ans += B//gcd_abc-1
if C != gcd_abc:
    ans += C//gcd_abc-1
print(ans)
