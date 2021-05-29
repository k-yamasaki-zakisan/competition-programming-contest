# https://atcoder.jp/contests/typical90/tasks/typical90_az

MOD = 10**9+7
N = int(input())
A_list = [list(map(int, input().split())) for _ in range(N)]
ans = 1
for a_list in A_list:
    ans *= sum(a_list)
    ans %= MOD
print(ans)
