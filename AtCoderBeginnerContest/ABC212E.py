# https://atcoder.jp/contests/abc212/tasks/abc212_e

MOD = 998244353

N, M, K = map(int, input().split())
UVs = [list(map(int, input().split())) for _ in range(M)]
e_root = [[] for _ in range(N)]
for u, v in UVs:
    if u > v:
        u, v = v, u
    u, v = u-1, v-1
    e_root[u].append(v)
    e_root[v].append(u)

dp = [0]*N
dp[0] = 1
dp_tmp = [0]*N

# 1日づつどの街に居られるのか場合の数をdp
for i in range(K):
    s = 0
    for j in range(N):
        s += dp[j]
    for j in range(N):
        dp_tmp[j] = s-dp[j]
        sz = len(e_root[j])
        for ii in range(sz):
            dp_tmp[j] -= dp[e_root[j][ii]]
        dp_tmp[j] %= MOD
    for j in range(N):
        dp[j] = dp_tmp[j]
print(dp[0])
