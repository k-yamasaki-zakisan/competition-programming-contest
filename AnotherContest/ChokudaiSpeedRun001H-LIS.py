#https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_h

import bisect

n = int(input())

seq = list(map(int,input().split()))

import bisect

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))
