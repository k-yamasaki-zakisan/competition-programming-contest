# https://atcoder.jp/contests/arc033/tasks/arc033_3

class Bit(object):
    def __init__(self,l:int):
        self.size = l
        self.bit = [0] * (self.size+1)

    def sum(self, i:int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i:int, x:int):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

    def __str__(self) -> str:
        return str(self.bit)

if __name__ == '__main__':

    N = int(input())
    TX = [list(map(int,input().split())) for _ in range(N)]
    
    bit = Bit(200000)
    for t,x in TX:
        if t == 1:
            bit.add(x,1)
        else:
            l, r = 0, 200000
            # x番目に小さい要素を２分探索
            while l+1<r:
                m = (l+r)//2
                if bit.sum(m) < x:
                    l = m
                else:
                    r = m
            print(r)
            # 要素の削除
            bit.add(r,-1)