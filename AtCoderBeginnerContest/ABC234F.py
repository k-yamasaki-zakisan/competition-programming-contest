# https://atcoder.jp/contests/abc234/tasks/abc234_f

MOD = 998244353
N = 20000
fact = [0 for _ in range(N)]
invfact = [0 for _ in range(N)]
fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD

invfact[N - 1] = pow(fact[N - 1], MOD - 2, MOD)

for i in range(N - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return (fact[n] * invfact[k] % MOD) * invfact[n - k] % MOD


S = input()
len_s = len(S)
cnt = [0]*26
for s in S:
    cnt[ord(s) - 97] += 1
dp = [[0] * (len_s + 1) for _ in range(27)]
dp[0][0] = 1
for i, c in enumerate(cnt, 1):
    for j in range(len_s+1):
        for k in range(c+1):
            if dp[i-1][j] == 0:
                break
            dp[i][j+k] += dp[i-1][j]*nCk(j+k, k)
            dp[i][j+k] %= MOD
print((sum(dp[-1]) - 1) % MOD)
