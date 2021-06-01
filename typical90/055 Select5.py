# https://atcoder.jp/contests/typical90/tasks/typical90_bc

from itertools import combinations
N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N-4):
    for j in range(i+1, N-3):
        for k in range(j+1, N-2):
            for l in range(k+1, N-1):
                for m in range(l+1, N):
                    v = A[i] * A[j] % P * A[k] % P * A[l] % P * A[m] % P
                    if v == Q:
                        ans += 1
print(ans)
