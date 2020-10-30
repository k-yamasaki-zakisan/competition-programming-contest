# https://atcoder.jp/contests/abc167/tasks/abc167_e

# M*(M-1)**(N-k-1)*(N-1)C(k)
# (M-1)**(N-k-1) == pow(M-1,N-k-1,MOD)
# (N-1)C(k) == comb(N-1,k)

N,M,K = map(int,input().split())
 
MAX = 2 * 10 ** 5 + 1
MOD = 998244353
 
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

ans = 0
for k in range(K+1):
    ans += M*pow(M-1,N-k-1,MOD)*comb(N-1,k)
    ans %= MOD
print(ans)