#https://atcoder.jp/contests/abc170/tasks/abc170_d

n=int(input())

a = list(map(int,input().split()))

a.sort()

if n > 1:
    if a[0] == a[1]:
        ans = 0
    else:
        ans = 1
else:
    print(1)
    exit()

for i in range(1,n):
    flag = True
    for j in range(i):
        if a[i] % a[j] == 0:
            flag = False
            break
        if int(a[i]**0.5)+1 < a[j]:  
            break
    if i == n-1:
        if flag and a[i] != a[i-1]:
            ans += 1
    else:
        if flag and a[i] != a[i-1] and a[i] != a[i+1]:
            ans += 1
print(ans)
