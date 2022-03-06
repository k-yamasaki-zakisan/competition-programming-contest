# https://atcoder.jp/contests/abc242/tasks/abc242_e

MOD2 = 998244353

T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    S_NUM = [ord(s) - ord("A") for s in S]
    if N == 1:
        ans.append(S_NUM[0] + 1)
        continue
    m = (N + 1) // 2
    dp = [0] * (m + 1)
    for i in range(m):
        dp[i + 1] = dp[i] * 26 % MOD2 + S_NUM[i]
    dp[-1] %= MOD2
    cnt = dp[-1]

    cnt += S_NUM[:m][::-1] <= S_NUM[-m:]
    ans.append(cnt % MOD2)
for a in ans:
    print(a)
