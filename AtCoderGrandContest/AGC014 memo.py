#https://atcoder.jp/contests/agc014/tasks/agc014_b

n,m = map(int,input().split())
ab = [0]*n
for _ in range(m):
    a, b = (int(x) for x in input().split())
    ab[a-1] += 1
    ab[b-1] += 1

flag = False

for i in ab:
    if i%2 == 1:
        flag = True
        break

if flag:
    print('NO')
else:
    print('YES')
