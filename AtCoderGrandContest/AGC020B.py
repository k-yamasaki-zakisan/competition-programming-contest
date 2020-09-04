#https://atcoder.jp/contests/agc020/tasks/agc020_b

K = int(input())
A = list(map(int,input().split()))
A.reverse()
if A[0] != 2:
    print(-1)
    exit()

low, high = 2, 3

for a in A:
    if high < a:
        print(-1)
        exit()
    elif a < low:
        low=(-((-low)//a))*a
        #print((-((-low)//a))*a, -((-low)//a))
        if low > high:
            print(-1)
            exit()
        high=max(low+a-1,high+a-1-high%a)
    else:
        low=a
        if low>high:
            print(-1)
            exit()
        high=low+a-1
print(low,high)
