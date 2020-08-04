#https://atcoder.jp/contests/abc060/tasks/arc073_b

N,W = map(int,input().split())
wv = []
base_w = float('inf')
for _ in range(N):
    w, v = (int(x) for x in input().split())
    wv.append([w, v])
    base_w = min(base_w, w)

dp = [[-10000000000 for i in range(100*3+1)] for j in range(N+1)]

dp[0][0] = 0

#横軸はお重さの合計、縦軸は何個選ぶか
for ws ,vs in wv:
    ws -= base_w
    for h in range(N+1, 0, -1):
        for w in range(100*3, -1, -1):
            if 0 <= w-ws:
                if dp[h-1][w-ws] != -10000000000:
                    dp[h][w] = max(dp[h][w], dp[h-1][w-ws]+vs)

ans = 0
for i in range(0,N+1):
    tmp_W = W-i*base_w
    #print(tmp_W, i)
    if 0 <= tmp_W:
        #print(dp[i][:tmp_W+1])
        tmp_max_V = max(dp[i][:tmp_W+1])
        ans = max(ans, tmp_max_V)
print(ans)   
