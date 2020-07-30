#https://atcoder.jp/contests/arc041/tasks/arc041_b

n,m = map(int,input().split())                
after_b = []
for _ in range(n):
    b=list(input())
    after_b.append(b)

before_a = [[0]*m for i in range(n)]

for y in range(1, n-1):
    for x in range(1, m-1):
        if y == 1 or y == 2:
            before_a[y][x] = int(after_b[y-1][x])-before_a[y-1][x-1]-before_a[y-1][x+1]
        else:
            before_a[y][x] = int(after_b[y-1][x])-before_a[y-1][x-1]-before_a[y-1][x+1]-before_a[y-2][x]

for i in range(n):
    print(''.join(map(str,before_a[i])))
