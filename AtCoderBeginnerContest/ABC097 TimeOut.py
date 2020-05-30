#https://atcoder.jp/contests/abc097/tasks/arc097_b

n,m = map(int,input().split())

p = list(map(int,input().split()))

root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

check = [-1]*n

ans = 0

for j in range(n):
    if check[j] != -1:
        continue
    stack=[j]
    check[j]=j
    while len(stack):
        v = stack.pop(0)
        for i in root[v]:
            if check[i] == -1:
                check[i]=j
                stack.append(i)
for k in range(n):
    if check[k] == check[p[k]-1] :
        ans += 1

print(ans)
