# https://atcoder.jp/contests/abc252/tasks/abc252_f

from heapq import heapify, heappop, heappush

N, L = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) < L:
    A.append(L - sum(A))
h = A[::-1]
heapify(h)
ans = 0
while 1 < len(h):
    x1 = heappop(h)
    x2 = heappop(h)
    ans += x1 + x2
    heappush(h, x1 + x2)
print(ans)
