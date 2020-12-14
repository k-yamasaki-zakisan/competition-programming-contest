# https://atcoder.jp/contests/abc185/tasks/abc185_f

class SegmentTree:
    def __init__(self, size, default=0):
        self.size = 2**(size-1).bit_length()
        self.default = default
        self.dat = [default]*(self.size*2)

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = (self.dat[i*2] ^ self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = (lres ^ self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = (self.dat[r] ^ rres)
            l >>= 1
            r >>= 1
        res = (lres ^ rres)
        return res

n, q = map(int, input().split())
a = list(map(int, input().split()))
s = SegmentTree(n)
for i in range(n):
    s.update(i, a[i])
for i in range(q):
    com, x, y = map(int, input().split())
    if com == 1:
        x = x-1
        s.update(x, a[x] ^ y)
        a[x] = a[x] ^ y
    else:
        print(s.query(x-1, y))