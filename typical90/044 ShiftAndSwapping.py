# https://atcoder.jp/contests/typical90/tasks/typical90_ar

from collections import deque
N, Q = map(int, input().split())
A = list(map(int, input().split()))
Txy = [list(map(int, input().split())) for _ in range(Q)]
A = deque(A)
for T, x, y in Txy:
    x, y = x-1, y-1
    if T == 1:
        A[x], A[y] = A[y], A[x]
    elif T == 2:
        a = A.pop()
        A.appendleft(a)
    else:
        print(A[x])
