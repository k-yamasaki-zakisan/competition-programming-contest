# https://atcoder.jp/contests/arc106/tasks/arc106_c

n,m = map(int,input().split())
if m < 0 :
    print(-1)
elif m == n:
    print(-1)
elif m == n-1 and n>=2:
    print(-1)
elif m == 0:
    # n個全てを被らないように出力するだけ
    for i in range(n):
        print(2*i+1,2*i+2)
else:
    # n-m-2を被らないように出力するだけ
    print(1, 10**7)
    print(10**7-2, 10**7-1)
    for i in range(1,m+1):
        print(2*i,2*i+1)
    for i in range(n-m-2):
        print(10**7+2*i+1, 10**7+2*i+2)