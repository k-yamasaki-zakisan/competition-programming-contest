#https://atcoder.jp/contests/past202004-open/tasks/past202004_f

import heapq

n=int(input())

memo = [[] for j in range(n)]

for _ in range(n):
  a, b = (int(x) for x in input().split())
  memo[a-1].append(-1*b)

ans = 0

ac_task = []

for i in range(n):
  for j in memo[i]:
    heapq.heappush(ac_task,j)
  ans -= heapq.heappop(ac_task)
  print(ans)
