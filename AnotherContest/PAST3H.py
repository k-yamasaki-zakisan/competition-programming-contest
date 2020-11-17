# https://atcoder.jp/contests/past202005-open/tasks/past202005_h

N,L = map(int,input().split())
X = list(map(int,input().split()))
T1,T2,T3 = map(int,input().split())
root = ['.']*(L+1)
for x in X:
    root[x] = '#'
dp = [10**10]*(L+1)
dp[0] = 0
for l in range(1,L+1):
    if 0<=l-1:
        tmp = dp[l-1]+T1
        if root[l-1] == '#':
            tmp += T3
        dp[l] = min(tmp,dp[l])
    if 0<=l-2:
        tmp = dp[l-2]+T1+T2
        if root[l-2] == '#':
            tmp += T3
        dp[l] = min(tmp,dp[l])
    if 0<=l-4:
        tmp = dp[l-4]+T1+T2*3
        if root[l-4] == '#':
            tmp += T3
        dp[l] = min(tmp,dp[l])
tmp = dp[L-1]+int(T1*0.5)+int(T2*0.5)
if root[L-1] == '#':
    tmp += T3
dp[L] = min(dp[L],tmp)
tmp = dp[L-2]+int(T1*0.5)+int(T2*1.5)
if root[L-2] == '#':
    tmp += T3
dp[L] = min(dp[L],tmp)
tmp = dp[L-3]+int(T1*0.5)+int(T2*2.5)
if root[L-3] == '#':
    tmp += T3
dp[L] = min(dp[L],tmp)
print(dp[-1])