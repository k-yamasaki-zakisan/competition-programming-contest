# https://atcoder.jp/contests/abc125/tasks/abc125_c
# gcd(0,A[i])はA[i]になる
# 左からの最大公約数配列と右からの最大公約数配列を作成して２つの配列の要素をずらして最大公約数をとると、一つだけ数を省いた状態の最大公約数を全て探索できる


import math
N = int(input())
A = list(map(int,input().split()))

gcd_l = [0]*(N+1)
gcd_r = [0]*(N+1)

for i in range(N):
    gcd_l[i+1] = math.gcd(gcd_l[i],A[i])

for i in range(N,0,-1):
    gcd_r[i-1] = math.gcd(gcd_r[i],A[i-1])

ans = 1
for i in range(N):
    ans = max(ans,math.gcd(gcd_l[i], gcd_r[i+1]))
print(ans)