# https://atcoder.jp/contests/typical90/tasks/typical90_bh

import bisect

N = int(input())
A = list(map(int, input().split()))
A_r = A[::-1]
LIS = [A[0]]
LIS_cont = [1]*N
LIS_r = [A_r[0]]
LIS_cont_r = [1]*N
for i in range(1, N):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
        LIS_cont[i] = len(LIS)
    else:
        pos = bisect.bisect_left(LIS, A[i])
        LIS[pos] = A[i]
        LIS_cont[i] = pos+1

    if A_r[i] > LIS_r[-1]:
        LIS_r.append(A_r[i])
        LIS_cont_r[i] = len(LIS_r)
    else:
        pos = bisect.bisect_left(LIS_r, A_r[i])
        LIS_r[pos] = A_r[i]
        LIS_cont_r[i] = pos+1
LIS_cont_r = LIS_cont_r[::-1]
ans = 0
for i in range(N):
    ans = max(ans, LIS_cont_r[i]+LIS_cont[i]-1)
print(ans)
