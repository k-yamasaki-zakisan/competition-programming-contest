# https://atcoder.jp/contests/typical90/tasks/typical90_ax

MOD = 10**9+7
N, L = map(int, input().split())
memo = [0]*100009
memo[1] = 1
for i in range(1, N+2):
    memo[i] %= MOD
    memo[i+1] += memo[i]
    if i+L < 100009:
        memo[i+L] += memo[i]
print(memo[N+1])
