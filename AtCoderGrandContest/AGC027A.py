#https://atcoder.jp/contests/agc027/tasks/agc027_a

n,x = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

sweets=0

ans = 0

for i in range(n):
    sweets += a[i]
    if sweets <= x:
        ans += 1
    else:
        break

if sweets < x:
    print(ans-1)
else:
    print(ans)
