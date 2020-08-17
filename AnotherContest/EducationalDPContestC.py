#https://atcoder.jp/contests/dp/tasks/dp_c

n=int(input())
 
ab = []
for _ in range(n):
    a, b, c = (int(x) for x in input().split())
    ab.append([a, b, c])
 
dp = [[0]*3 for j in range(n+1)]
 
for i in range(n):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i+1][k] = max([dp[i+1][k], dp[i][j]+ab[i][k]])
 
print(max(dp[n]))
