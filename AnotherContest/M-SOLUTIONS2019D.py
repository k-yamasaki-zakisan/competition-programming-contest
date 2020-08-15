#https://atcoder.jp/contests/m-solutions2019/tasks/m_solutions2019_d

from collections import deque

N = int(input())

root = [[] for i in range(N)]
for _ in range(N-1):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

c = list(map(int,input().split()))
c.sort(reverse=True)

stack=deque([0])
check = [-1]*N
check[0] = 0

while len(stack)>0:
    v = stack.popleft()
    for i in root[v]:
        if check[i] == -1:
            check[i]=check[v]+1
            stack.append(i)

keyCheck = [(i,check[i]) for i in range(N)]
keyCheck.sort(key=lambda t:t[1])
#print(keyCheck)
ans = [-1]*N
for i in range(N):
    ans[keyCheck[i][0]] = c[i]

print(sum(c[1:]))
print(*ans)
