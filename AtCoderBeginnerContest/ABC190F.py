# https://atcoder.jp/contests/abc190/tasks/abc190_f

class Bit(object):
    def __init__(self, l: int):
        self.size = l
        self.bit = [0] * (self.size+1)

    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i: int, x: int):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self) -> str:
        return str(self.bit)


if __name__ == '__main__':

    N = int(input())
    A = list(map(int, input().split()))
    A = [a+1 for a in A]

    ans = 0
    bit = Bit(len(A))
    for i, v in enumerate(A):
        ans += i - bit.sum(v)
        bit.add(v, 1)

    for i in range(N):
        if i == 0:
            print(ans)
            continue
        a = A[i-1]-1
        ans -= a
        ans += N-1-a
        print(ans)
