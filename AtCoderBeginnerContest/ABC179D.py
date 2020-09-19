#https://atcoder.jp/contests/abc179/tasks/abc179_d

mod = 998244353
N,K = map(int,input().split())
move = [list(map(int,input().split())) for _ in range(K)]

dp = [0]*(N+1)
dp_sum = [0]*(N+1)
dp[1] = dp_sum[1] = 1
for i in range(2,N+1):
    for l,r in move:
        #累積和を追加
        if 0<i-l:
            dp[i] += dp_sum[i-l]
        #範囲外の値をひく
        if 0<i-r-1:
            dp[i] -= dp_sum[i-r-1]
        dp[i] %= mod
    dp_sum[i] = dp_sum[i-1] + dp[i]
            
print(dp[-1]%mod)
