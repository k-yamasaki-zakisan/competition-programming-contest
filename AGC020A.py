#https://atcoder.jp/contests/agc020/tasks/agc020_a

n,a,b = map(int,input().split())

if abs(a-b)%2==1:
    print('Borys')
else:
    print('Alice')
