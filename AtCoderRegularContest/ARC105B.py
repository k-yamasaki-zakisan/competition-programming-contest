#https://atcoder.jp/contests/arc105/tasks/arc105_b

import math

N = int(input())
A = list(map(int,input().split()))
if N == 1:
    print(A[0])
    exit()

max_gcd = math.gcd(A[0], A[1])
for i in range(2,len(A)):
    max_gcd = math.gcd(max_gcd, A[i])

print(max_gcd)