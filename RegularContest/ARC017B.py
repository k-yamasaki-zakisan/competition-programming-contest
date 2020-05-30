#https://atcoder.jp/contests/arc017/tasks/arc017_2

n,k = map(int,input().split())
ab = []
for _ in range(n):
    s=int(input())
    ab.append(s)

check = 1

start = 0

ans = 0

flag = True

while check < n:
    if ab[check] <= ab[check-1]:
        start = check
    if check-start == k-1:
        ans += 1
        start += 1
    check += 1
    
print(ans)
