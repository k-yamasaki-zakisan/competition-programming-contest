#https://atcoder.jp/contests/agc024/tasks/agc024_a

a,b,c,k = map(int,input().split())

if k%2==1:
    print(b-a)
else:
    print(a-b)
