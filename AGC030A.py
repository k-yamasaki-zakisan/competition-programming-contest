#https://atcoder.jp/contests/agc030/tasks/agc030_a

a,b,c = map(int,input().split())

if c<=b+a:
    print(b+c)
else:
    print(a+b*2+1)
