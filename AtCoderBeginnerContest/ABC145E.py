#https://atcoder.jp/contests/abc145/tasks/abc145_e

n,t=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(n)]
ab.sort()

dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(n):
    wi, vi = ab[i]
    for j in range(t+1):
        if j + wi <= t:
            dp[i+1][j+wi] = max(dp[i+1][j+wi], dp[i][j]+vi)
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])

ans = 0

#最終商品をラストオーダ(t-1)で注文する
for i ,(wi,vi) in enumerate(ab):
    ans = max(ans, dp[i][t-1]+vi)
   
print(ans)
