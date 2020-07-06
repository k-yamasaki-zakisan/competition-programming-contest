#https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_a

x,y = map(int,input().split())

if x >= 1+2*(y-1):
    print('YES')
else:
    print('NO')
