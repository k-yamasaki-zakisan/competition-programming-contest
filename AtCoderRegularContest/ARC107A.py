# https://atcoder.jp/contests/arc107/tasks/arc107_a

MOD = 998244353

A,B,C = map(int,input().split())

a = (A*(A+1)//2)%MOD
b = (B*(B+1)//2)%MOD
c = (C*(C+1)//2)%MOD

print((a*b*c)%MOD)