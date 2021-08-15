# https://atcoder.jp/contests/abc214/tasks/abc214_e

from heapq import heappush, heappop
from bisect import bisect_left
from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    d = defaultdict(list)

    ls = [0]*N
    rs = [0]*N
    for i in range(N):
        l, r = map(int, input().split())
        d[l].append(i)

        ls[i] = l
        rs[i] = r

    ls.sort()

    pq = []
    ng_flag = False

    cur = 0
    j = 0
    for i in range(10**8):
        if cur in d:
            for x in d[cur]:
                heappush(pq, rs[x])
        if pq:
            if heappop(pq) < cur:
                ng_flag = True
                break
            cur += 1
        else:
            j = bisect_left(ls, cur, j)
            if j <= N-1:
                cur = ls[j]
            else:
                break

    if ng_flag:
        print('No')
    else:
        print('Yes')
