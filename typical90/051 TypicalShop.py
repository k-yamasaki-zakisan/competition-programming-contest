# https://atcoder.jp/contests/typical90/tasks/typical90_ay

from itertools import combinations
from bisect import bisect_right

N, K, P = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    if A[0] <= P:
        print(1)
    else:
        print(0)
    exit()

A_1 = A[:N//2]
A_2 = A[N//2:]
A_1_combs, A_2_combs = [[0]], [[0]]
for i in range(1, len(A_1)+1):
    tmp_combs = []
    for v in combinations(A_1, i):
        tmp_combs += [sum(v)]
    A_1_combs.append(tmp_combs)
for i in range(1, len(A_2)+1):
    tmp_combs = []
    for v in combinations(A_2, i):
        tmp_combs += [sum(v)]
    A_2_combs.append(tmp_combs)

ans = 0
for i_1 in range(K+1):
    i_2 = K-i_1
    try:
        A_2_comb = A_2_combs[i_2]
        A_2_comb.sort()
        for a in A_1_combs[i_1]:
            index = bisect_right(A_2_comb, P-a)
            ans += index
    except:
        continue
print(ans)
