#https://atcoder.jp/contests/agc014/tasks/agc014_a

a,b,c = map(int,input().split())
ans = 0
while a%2==b%2==c%2==0:
    a,b,c = (b+c)//2, (a+c)//2, (a+b)//2
    ans += 1
    if ans >100:
        ans = -1
        break
print(ans)
