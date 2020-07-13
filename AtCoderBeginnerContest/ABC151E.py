#https://atcoder.jp/contests/abc151/tasks/abc151_e

N, K = map(int,input().split())

A = list(map(int,input().split()))
 
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

### nCrの計算  
def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD

A.sort()
ans = 0
for i in range(N):
    if i >= K - 1:
        ans += comb(i, K - 1) * A[i]
    if i + K - 1 < N:
        ans -= comb(N - i - 1, K - 1) * A[i]
    ans %= MOD
print(ans)
 
