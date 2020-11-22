# https://atcoder.jp/contests/abc184/tasks/abc184_c

R1,C1 = map(int,input().split())
R2,C2 = map(int,input().split())

if R1 == R2 and C1 == C2:
    print(0)
elif abs(R2-R1)+abs(C2-C1) <= 3 or R1+C1==R2+C2 or R1-C1==R2-C2:
    print(1)
elif (R1+R2+C1+C2)%2==0:
    print(2)
elif abs(R2-R1)+abs(C2-C1) <= 6:
    print(2)
elif abs(R2-R1+C2-C1) <= 3 or abs(R2-R1-(C2-C1)) <= 3:
    print(2)
else:
    print(3)