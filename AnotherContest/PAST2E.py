#https://atcoder.jp/contests/past202004-open/tasks/past202004_e

n=int(input())

t = list(map(int,input().split()))

memo = [0]*n

for i in range(n):
  memo[i] = t[i]-1

ans = [0]*n

for i in range(n):
  count = 1
  search_i = i
  if i == memo[i]:
    ans[i] = count
    continue

  while i != memo[search_i]:
    count += 1
    search_i = memo[search_i]
  ans[i] = count

print(*ans)
