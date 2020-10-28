# https://atcoder.jp/contests/abc142/tasks/abc142_e

N,M = map(int,input().split())
E = []
for i in range(M):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    E.append([a,c])

INF = 10**10
dp = [INF]*2**N
dp[0] = 0
for i in range(2**N):
    if dp[i] == INF:
        continue
    for a,c in E:
        bit = i
        for j in c:
            # 過去の結果で箱を開けられている場合を拾ってくる
            bit |= 2**(N-j)
        dp[bit] = min(dp[bit], dp[i]+a)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])