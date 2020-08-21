#https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j

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

    n = int(input())
    a = list(map(int,input().split()))
    
    ans = 0
    bit = Bit(len(a))
    for i,v in enumerate(a):
        ans += i - bit.sum(v)
        bit.add(v,1)

print(ans)
