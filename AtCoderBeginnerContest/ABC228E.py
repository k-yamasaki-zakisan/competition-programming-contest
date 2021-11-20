# https://atcoder.jp/contests/abc228/tasks/abc228_e

MOD = 998244353

N, K, M = map(int, input().split())
if M % MOD == 0:
    print(0)
    exit()
tmp = pow(K, N, MOD-1)
print(pow(M, tmp, MOD))
