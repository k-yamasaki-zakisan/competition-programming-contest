#https://atcoder.jp/contests/abc097/tasks/arc097_b

n,m = map(int,input().split())

p = list(map(int,input().split()))

root = [[] for i in range(n)]
for _ in range(m):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1)

dp = [False]*n

ans = 0

for j in range(n):
    if dp[j]:
        continue
    check = [-1]*n
    check[j] = 0
    stack=[j]
    dp[j] = True
    while len(stack):
        v = stack.pop()
        for i in root[v]:
            if check[i] == -1:
                dp[i] = True
                check[i]=i
                stack.append(i)
    for k in range(n):
        if check[k] != -1 and check[p[k]-1] != -1:
            ans += 1

print(ans)
