# https://atcoder.jp/contests/abc180/tasks/abc180_e
# 巡回セールスマン問題

V = int(input())
#コストフォーマット作成
XYZ = [list(map(int,input().split())) for _ in range(V)]
tmp_cost = []
for i in range(V):
    for j in range(V):
        if i == j:
            continue
        a,b,c = XYZ[i]
        p,q,r = XYZ[j]
        tmp = abs(a-p)+abs(b-q)+max(0,r-c)
        tmp_cost.append([i,j,tmp])

INF = 10**10
cost = [[INF]*V for _ in range(V)] # 重み
for s,t,d in tmp_cost:
    cost[s][t] = d

dp = [[-1] * V for _ in range(1<<V)] # dp[S][v]

def dfs(S, v, dp):
    if dp[S][v] != -1: # 訪問済みならメモを返す
        return dp[S][v]
    if S==(1<<V)-1 and v==0: # 全ての頂点を訪れて頂点0に戻ってきた
        return 0 # もう動く必要はない

    res = INF
    for u in range(V):
        if S>>u & 1 == 0: # 未訪問かどうか
            res = min(res, dfs(S|1<<u, u, dp)+cost[v][u])
    dp[S][v] = res
    return res

ans = dfs(0, 0, dp) # 頂点0からスタートする。ただし頂点0は未訪問とする
if ans == INF:
    print(-1)
else:
    print (ans)