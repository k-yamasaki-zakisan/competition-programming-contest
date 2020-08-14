#https://atcoder.jp/contests/abc069/tasks/arc080_b

H,W = map(int,input().split())

N = int(input())

a = list(map(int,input().split()))

dp = [[0]*W for _ in range(H)]

strate = True
w = 0
h = 0
dp[0][0] = 1

for key,value in enumerate(a):
    if key == 0:
        count = 1
        if value == 1:
            continue       
    else:
        count = 0

    while count < value:
        count += 1
        if strate:
            if w < W-1:
                w += 1
            elif w == W-1:
                strate = False
                h += 1
        else:
            if 0 < w:
                w -= 1
            elif w == 0:
                strate = True
                h += 1

        dp[h][w] = key+1
                
for aa in dp:
    print(*aa)
