#https://atcoder.jp/contests/agc035/tasks/agc035_a

n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
if b.count(0)==n:
    print("Yes")
elif n%3==0:
    if b.count(0)==n//3 and b.count(b[n-1])==n-(n//3):
        print("Yes")
    elif b[0]^b[n//3]^b[n-1]==0 and b.count(b[0])==n//3 and b.count(b[n//3])==n//3 and b.count(b[n-1])==n//3:
        print("Yes")
    else:
        print("No")
else:
    print("No")
