#https://atcoder.jp/contests/abc138/tasks/abc138_d

n,q = map(int,input().split())
 
root = [[] for i in range(n)]
for _ in range(n-1):
    a, b = (int(x) for x in input().split())
    root[b-1].append(a-1)
    root[a-1].append(b-1) 
 
 
dp = [0]*n
for _ in range(q):
    p, x = (int(x) for x in input().split())
    dp[p-1] += x
 
stack=[0]
check = [-1]*n
check[0] = 0
 
while len(stack):
    v = stack.pop()
    for i in root[v]:
        if i != check[i]:
            dp[i] += dp[v]
            check[i]=i
            stack.append(i)
 
print(' '.join(map(str,dp)))
