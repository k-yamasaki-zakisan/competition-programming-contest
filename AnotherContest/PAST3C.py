x,y,n = map(int,input().split())

ans = x
for i in range(n-1):
    ans *= y
    if 10**9 < ans:
        break

if 10**9 < ans:
    print('large')
else:
    print(ans)