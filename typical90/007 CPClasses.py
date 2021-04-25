# https://atcoder.jp/contests/typical90/tasks/typical90_g

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
A += [10**11]
Q = int(input())
B = [int(input()) for _ in range(Q)]
for b in B:
    pos = bisect_left(A, b)
    if pos == 0:
        ans = A[0]-b
    else:
        ans = min(A[pos]-b, b-A[pos-1])
    print(ans)
