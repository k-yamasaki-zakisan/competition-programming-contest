#https://atcoder.jp/contests/abc038/tasks/abc038_c


n=int(input())

t = list(map(int,input().split()))

count = [0]*(n+1)

for i in range(n+1):
    count[i] = i+count[i-1]

ans = 0

memo = 1

for i in range(n-1):
    if t[i] < t[i+1]:
        memo += 1
    else:
        ans += count[memo]
        memo = 1
ans += count[memo]

print(ans)
        
