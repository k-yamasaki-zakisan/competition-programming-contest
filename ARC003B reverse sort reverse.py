#https://atcoder.jp/contests/arc003/tasks/arc003_2

n=int(input())
ab = []
for _ in range(n):
    s=list(input())
    s.reverse()
    s=''.join(map(str,s))
    ab.append(s)

ab.sort()

for i in ab:
    i = list(i)
    i.reverse()
    print(''.join(map(str,i)))
