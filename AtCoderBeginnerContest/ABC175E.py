#https://atcoder.jp/contests/abc175/tasks/abc175_e

#AC code
R,C,K = map(int,input().split())

item = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(K):
    r,c,v = map(int,input().split())
    item[r][c] = v

dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

for h in range(R+1):
    for w in range(C+1):
        for k in range(4):
            position = dp[k][h][w]
            if h+1 <= R:
                # 移動先のアイテムを取らない場合
                dp[0][h+1][w] = max(dp[0][h+1][w], position)
                 # 移動先のアイテムを取る場合
                dp[1][h+1][w] = max(dp[1][h+1][w], position+item[h+1][w])
            if w+1 <= C:
                # 移動先のアイテムを取らない場合
                dp[k][h][w+1] = max(dp[k][h][w+1], position)
                # 現在のkが3未満のときのみ, 移動先のアイテムを取ることが可能
                if k < 3:
                    dp[k+1][h][w+1] = max(dp[k+1][h][w+1], position+item[h][w+1])

ans = 0
for k in range(4):
    ans = max(ans, dp[k][-1][-1])

print(ans)



#WA code
import copy
import heapq

R,C,K = map(int,input().split())

cost = [[0 for i in range(C)] for j in range(R)] 

dp = [[0 for i in range(C)] for j in range(R+1)]

pick_up = [[[] for i in range(C)] for j in range(R)] 

for _ in range(K):
    r,c,v = map(int,input().split())
    r,c = r-1,c-1
    cost[r][c] = v

for h in range(R):
    for w in range(C):
        if w == 0:
            dp[h+1][w] = dp[h][w]+cost[h][w]
            if cost[h][w] != 0:
                heapq.heappush(pick_up[h][w],cost[h][w])
        else:
            if len(pick_up[h][w-1]) < 3:
                dp[h+1][w] = max(dp[h][w]+cost[h][w], dp[h+1][w-1]+cost[h][w])
                if cost[h][w] != 0:
                    if dp[h+1][w] == dp[h][w]+cost[h][w]:
                        heapq.heappush(pick_up[h][w],cost[h][w])
                    else:
                        tmp_array1 = copy.copy(pick_up[h][w-1])
                        heapq.heappush(tmp_array1,cost[h][w])
                        pick_up[h][w] = copy.copy(tmp_array1)
                else:
                    if dp[h+1][w] == dp[h][w]+cost[h][w]:
                        continue
                    else:
                        pick_up[h][w] = pick_up[h][w-1]
                    
            else:
                if cost[h][w] != 0:
                    tmp_array2 = copy.copy(pick_up[h][w-1])
                    minus = sum(tmp_array2)
                    heapq.heappush(tmp_array2,cost[h][w])
                    heapq.heappop(tmp_array2)
                    dp[h+1][w] = max(dp[h][w]+cost[h][w], dp[h+1][w-1]-minus+sum(tmp_array2))
                    if dp[h+1][w] == dp[h][w]+cost[h][w]:
                        heapq.heappush(pick_up[h][w],cost[h][w])
                    else:
                        pick_up[h][w] = copy.copy(tmp_array2)
                    
                else:
                    dp[h+1][w] = max(dp[h][w]+cost[h][w], dp[h+1][w-1]+cost[h][w])
                    if dp[h+1][w] == dp[h][w]:
                        continue
                    else:
                        pick_up[h][w] = copy.copy(pick_up[h][w-1])
    
            
print(dp[-1][-1])
for i in dp:
    print(*i)
print('-----------------')
for i in cost:
    print(*i)
print('-----------------')
for i in pick_up:
    print(*i)
