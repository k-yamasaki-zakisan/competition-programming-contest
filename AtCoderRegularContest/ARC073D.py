#https://atcoder.jp/contests/arc073/tasks/arc073_b

N, W = (int(x) for x in input().split())
dp = [[-1 for i in range(301)] for j in range(N+1)]
dp[0][0] = 0
for k in range(N):
    w, v = (int(x) for x in input().split())
    if k == 0:
        base_w = w
    for i in range(N)[::-1]:    
        for j in range(301)[::-1]:
            if dp[i][j]!=-1:
                dp[i+1][j+w-base_w] = max([dp[i][j]+v, dp[i+1][j+w-base_w]])
        
ans=0
for index,item in enumerate(dp):
    if W-index*base_w+1<=0:
        break
    ans=max(max(item[:W-index*base_w+1]),ans)

print(ans)
