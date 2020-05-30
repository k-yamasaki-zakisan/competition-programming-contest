#https://atcoder.jp/contests/caddi2018/tasks/caddi2018_b

N=int(input())
 
flag=False
for _ in range(N):
    a=int(input())
    if a%2==1:
        flag=True
if flag:
    print('first')
else:
    print('second')
