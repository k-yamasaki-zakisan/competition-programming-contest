#https://atcoder.jp/contests/abc126/tasks/abc126_e

from collections import deque
 
n,m = map(int,input().split())
 
root = [[] for i in range(n)]
for _ in range(m):
    a, b ,c = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 

check = [-1]*n

ans = 0

for j in range(n):
  if check[j] != -1: continue
  ans += 1
  check[j] = 1
  stack=deque([j])
  check[0] = 0
  while len(stack)>0:
      v = stack.popleft()
      for i in root[v]:
          if check[i] == -1:
              check[i] = 1
              stack.append(i)
for i in check:
  if i == -1:
    ans += 1
print(ans)
