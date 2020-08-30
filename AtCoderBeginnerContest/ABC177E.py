#https://atcoder.jp/contests/abc177/tasks/abc177_e

def prime(p):
    memo = set()
    for i in range(2,(int(p**0.5)+1)):
        while p%i==0:
            p //= i
            memo.add(i)
    if p != 1:
        memo.add(p)
    return memo

from math import gcd

N = int(input())

A = list(map(int,input().split()))

tmp_gcd = A[0]

#最大公約数が２以上かを判定
for i in range(1,N):
    tmp_gcd = gcd(tmp_gcd, A[i])

if 1 < tmp_gcd:
    print('not coprime')
    exit()

#素因数に被りがあるか判定
servive_prime = set()
for a in A:
    now_prime = prime(a)
    ls,ln = len(servive_prime), len(now_prime)
    servive_prime.update(now_prime)
    if len(servive_prime) < ls + ln:
        print('setwise coprime')
        exit()

#素因数被りがない場合
print('pairwise coprime')
