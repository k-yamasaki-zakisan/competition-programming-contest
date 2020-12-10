# https://atcoder.jp/contests/abc150/tasks/abc150_d

import math
N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [a//2 for a in A]
lcm = 1
for a in A:
    lcm = lcm*a//math.gcd(lcm,a)
for a in A:
    if (lcm//a)%2==0:
        print(0)
        exit()

ans = M//lcm-(M//(lcm*2))
print(ans)