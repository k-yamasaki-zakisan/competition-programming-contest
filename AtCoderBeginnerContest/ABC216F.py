# https://atcoder.jp/contests/abc216/tasks/abc216_f

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [(A[i], B[i]) for i in range(N)]
AB = sorted(AB, key=lambda x: x[0])

ans = 0
mx = max(A)
dp = [0]*(mx+1)
dp[0] = 1
for i in range(N):
    a, b = AB[i]
    for j in range(mx, -1, -1):
        if j + b <= mx:
            dp[j+b] += dp[j]
            dp[j+b] %= MOD
            if j+b <= a:
                ans += dp[j]
                ans %= MOD
print(ans)
