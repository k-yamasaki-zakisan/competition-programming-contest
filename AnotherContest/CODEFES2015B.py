# https://atcoder.jp/contests/code-festival-2015-morning-middle/tasks/cf_2015_morning_easy_d

N = int(input())
S = input()

ans = 10**10
for m in range(N+1):
    L,R = S[:m], S[m:]
    dp = [[0] * (len(R) + 1) for _ in range(len(L) + 1)]
    for l, ls in enumerate(L, start=1):
        for r,rs in enumerate(R, start=1):
            if ls == rs:
                dp[l][r] = dp[l-1][r-1]+1
            else:
                dp[l][r] = max(dp[l-1][r],dp[l][r-1])
    ans = min(ans, N-2*dp[-1][-1])

print(ans)