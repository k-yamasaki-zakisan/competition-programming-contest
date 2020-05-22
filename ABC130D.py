#https://atcoder.jp/contests/abc130/tasks/abc130_d

n,k = map(int,input().split())
 
a = list(map(int,input().split()))
 
memo = 0
 
start = 0
 
ans = 0
 
for i in range(n):
    memo += a[i]
    if k<=memo:
        while k<=memo:
            ans += n-i
            memo -= a[start]
            start += 1
print(ans)
