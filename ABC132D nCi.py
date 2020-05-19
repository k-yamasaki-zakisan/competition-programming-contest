#https://atcoder.jp/contests/abc132/tasks/abc132_d

import math
 
def combination(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
 

n, k = map(int, input().split())
 
for i in range(1, k + 1):
    if i <= n - k + 1:
        print(combination(n-k+1,i) * combination(k-1,i-1) % 1000000007)
    else:
        print(0)
