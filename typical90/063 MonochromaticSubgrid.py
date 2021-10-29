# https://atcoder.jp/contests/typical90/tasks/typical90_bk


N, Q = map(int, input().split())
A = list(map(int, input().split()))
LRV = [list(map(int, input().split())) for _ in range(Q)]
sa = []
for i in range(1, N):
    sa.append(A[i]-A[i-1])
total = sum([abs(s) for s in sa])
for l, r, v in LRV:
    l, r = l-1, r-1
    if 0 < l:
        total -= abs(sa[l-1])
        sa[l-1] = sa[l-1]+v
        total += abs(sa[l-1])
    if r < N-1:
        total -= abs(sa[r])
        sa[r] = sa[r]-v
        total += abs(sa[r])
    print(total)
