# https://atcoder.jp/contests/typical90/tasks/typical90_bh

import bisect

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]
LIS_cnt = [1]*N
for i in range(1, len(A)):
    a = A[i]
    if LIS[-1] < a:
        LIS.append(a)
        LIS_cnt[i] = len(LIS)
    else:
        b_i = bisect.bisect_left(LIS, a)
        LIS[b_i] = a
        LIS_cnt[i] = b_i+1

A_r = A[::-1]
r_LIS = [A_r[0]]
r_LIS_cnt = [1]*N
for i in range(1, len(A_r)):
    a = A_r[i]
    if r_LIS[-1] < a:
        r_LIS.append(a)
        r_LIS_cnt[i] = len(r_LIS)
    else:
        b_i = bisect.bisect_left(r_LIS, a)
        r_LIS[b_i] = a
        r_LIS_cnt[i] = b_i+1
r_LIS_cnt = r_LIS_cnt[::-1]

ans = 0
for i in range(N):
    ans = max(ans, LIS_cnt[i]+r_LIS_cnt[i]-1)
print(ans)
