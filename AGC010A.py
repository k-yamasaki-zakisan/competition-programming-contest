#https://atcoder.jp/contests/agc010/tasks/agc010_a

n=int(input())

t = list(map(int,input().split()))

count = 0

for i in t:
    if i%2==1:
        count += 1
if count%2==1:
    print('NO')
else:
    print('YES')
