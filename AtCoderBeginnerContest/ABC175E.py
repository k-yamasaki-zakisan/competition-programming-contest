#https://atcoder.jp/contests/abc175/tasks/abc175_e

import heapq

R,C,K = map(int,input().split())

cost = [[0 for i in range(C)] for j in range(R)] 

dp = [[0 for i in range(C)] for j in range(R+1)]

for _ in range(K):
    r,c,v = map(int,input().split())
    r,c = r-1,c-1
    cost[r][c] = v

for h in range(R):
    tmp_pick = []
    for w in range(C):
        if cost[h][w] != 0:
            heapq.heappush(tmp_pick,cost[h][w])
        if len(tmp_pick) <= 3:
            if w == 0:
                dp[h+1][w] = dp[h][w]+cost[h][w]
            else:
                dp[h+1][w] = max(dp[h][w]+cost[h][w], dp[h+1][w-1]+cost[h][w])
        else:
            min_value = heapq.heappop(tmp_pick)
            dp[h+1][w] = max(dp[h][w]+cost[h][w], dp[h+1][w-1]+cost[h][w]-min_value)
            
print(dp[-1][-1])
