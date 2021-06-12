# https://atcoder.jp/contests/typical90/tasks/typical90_bl

N, Q = (int(x) for x in input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]
B = [0]*(N+9)
for i in range(1, N):
    B[i] = (A[i]-A[i-1])

dist = sum([abs(b) for b in B])
for l, r, v in LRV:
    now = abs(B[l-1]) + abs(B[r])
    if 2 <= l:
        B[l-1] += v
    if r <= N-1:
        B[r] -= v
    next = abs(B[l-1]) + abs(B[r])
    dist += next - now
    print(dist)
