#https://atcoder.jp/contests/abc015/tasks/abc015_4

w=int(input())
 
n,k = map(int,input().split())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
 
dp = [[0 for i in range(w+1)] for j in range(k+1)]
 
for a, b in ab:
    for i in range(k, 0, -1):
        for j in range(w+1):
            if a <= j:
                dp[i][j] = max(dp[i-1][j-a]+b, dp[i][j])
print(dp[-1][-1])
