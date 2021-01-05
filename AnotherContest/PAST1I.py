# https://atcoder.jp/contests/past201912-open/tasks/past201912_i

INF = 10**10
N, M = map(int, input().split())
SC = []
for _ in range(M):
    S, C = map(str, input().split())
    pair = []
    for i, s in enumerate(S):
        if s == 'Y':
            pair.append(i+1)
    SC.append((pair, int(C)))

ans = INF
dp = [INF]*(2**N)
dp[0] = 0
for i in range(2**N):
    if dp[i] == INF:
        continue
    for a, c in SC:
        bit = i
        for j in a:
            bit |= 2**(N-j)
        dp[bit] = min(dp[bit], dp[i]+c)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
