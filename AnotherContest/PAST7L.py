# https://atcoder.jp/contests/past202107-open/tasks/past202107_l

from collections import defaultdict


class SegmentTree:
    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res


N, Q = map(int, input().split())
A = list(map(int, input().split()))
TXY = [list(map(int, input().split())) for _ in range(Q)]
S = SegmentTree(N, min, 2**31-1)
memo = defaultdict(set)
for i, a in enumerate(A):
    S.update(i, a)
    memo[a].add(i+1)

for t, x, y in TXY:
    if t == 1:
        S.update(x-1, y)
        memo[A[x-1]].remove(x)
        A[x-1] = y
        memo[y].add(x)
    else:
        min_num = S.query(x-1, y)
        tmp = list(memo[min_num])
        ans = sorted([r for r in tmp if x <= r <= y])
        print(len(ans), *ans)
