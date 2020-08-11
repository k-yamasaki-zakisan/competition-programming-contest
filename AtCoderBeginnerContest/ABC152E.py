#https://atcoder.jp/contests/abc152/tasks/abc152_e

import math
 
mod = 1000000007
 
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
 
n=int(input())
 
a = list(map(int,input().split()))
 
memo = a[0]
 
for i in range(1,n):
    memo = lcm(memo,a[i])
 
ans = 0
 
for i in range(n):
    ans += memo*pow(a[i], mod-2, mod)%mod
    ans %= mod
 
print(ans)
