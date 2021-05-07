# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
memo = defaultdict(int)
tail = 0
ans = 0
kind = 0
len_long = 0
for i, a in enumerate(A):
    memo[a] += 1
    len_long += 1
    if memo[a] == 1:
        kind += 1
    while K < kind and tail < N:
        tail_a = A[tail]
        memo[tail_a] -= 1
        len_long -= 1
        if memo[tail_a] == 0:
            kind -= 1
        tail += 1
    ans = max(ans, len_long)
print(ans)
