# https://atcoder.jp/contests/typical90/tasks/typical90_o

MAX = 10 ** 5 + 1
MOD = 10 ** 9 + 7

fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD

finv = [0] * (MAX + 1)
finv[MAX] = pow(fac[MAX], MOD - 2, MOD)

for i in range(MAX, 0, -1):
    finv[i - 1] = finv[i] * i % MOD


def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD


N = int(input())
for k in range(1, N+1):
    tmp = 0
    for i in range(1, N//k+2):
        s = N - (k - 1) * (i - 1)
        tmp += comb(s, i)
        tmp %= MOD
    print(tmp)
