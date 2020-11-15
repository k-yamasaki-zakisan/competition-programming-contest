# https://atcoder.jp/contests/abc183/tasks/abc183_e

mod = 10**9+7
H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
dp_tate = [[0]*(W) for _ in range(H)]
dp_yoko = [[0]*(W) for _ in range(H)]
dp_nana = [[0]*(W) for _ in range(H)]
dp = [[0]*(W) for _ in range(H)]
dp_tate[0][0] = dp_yoko[0][0] = dp_nana[0][0]= dp[0][0] = 1
if S[0][1] == '.':
    dp_tate[0][1] = dp_yoko[0][1] = dp_nana[0][1]= dp[0][1] = 1
if S[1][0] == '.':
    dp_tate[1][0] = dp_yoko[1][0] = dp_nana[1][0]= dp[1][0] = 1
for h in range(H):
    for w in range(W):
        if S[h][w] == '#' or h == w == 0 or (h == 0 and w == 1) or (h == 1 and w == 0):
            continue
        if h == 0:
            if dp_yoko[h][w-1] == 0:
                continue 
            dp_yoko[h][w] = dp_yoko[h][w-1]*2%mod
            dp[h][w] = dp_yoko[h][w]
            dp_tate[h][w] = dp_yoko[h][w]
            dp_nana[h][w] = dp_yoko[h][w]
        elif w == 0:
            if dp_tate[h-1][w] == 0:
                continue
            dp_tate[h][w] = dp_tate[h-1][w]*2%mod
            dp[h][w] = dp_tate[h][w]
            dp_nana[h][w] = dp_tate[h][w]
            dp_yoko[h][w] = dp_tate[h][w]
        else:
            dp[h][w] = (dp_nana[h-1][w-1]+dp_tate[h-1][w]+dp_yoko[h][w-1])%mod
            dp_nana[h][w] =  dp[h][w]+dp_nana[h-1][w-1]
            dp_tate[h][w] =  dp[h][w]+dp_tate[h-1][w]
            dp_yoko[h][w] =  dp[h][w]+dp_yoko[h][w-1]

print(dp[-1][-1]%mod)