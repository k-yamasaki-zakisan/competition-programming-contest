#https://yukicoder.me/problems/no/3009

n=int(input())

a = list(map(int,input().split()))

head = 0

check = {a[0]:0}

ans = 0

for tail in range(1,n):
    if a[tail] in check and head <= check[a[tail]]:
        ans = max(ans, tail-head)
        head = check[a[tail]]+1    

    check[a[tail]] = tail
    #print(ans,tail,head)
ans = max(ans, n-head)

print(ans)
