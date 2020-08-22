#https://atcoder.jp/contests/abc176/tasks/abc176_d

import copy
 
H, W = [int(x) for x in input().split()]

Ch,Cw = map(int,input().split())

Ch,Cw = Ch-1,Cw-1

Dh,Dw = map(int,input().split())

Dh,Dw = Dh-1,Dw-1

cell = [list(input()) for i in range(H)]

dp = [[-1]*W for _ in range(H)]

copy_stack = [[Ch,Cw]]

nstack = []

dp[Ch][Cw] = 0

#通常の縦横移動
def search(stack):
    while len(stack) > 0:
        h,w = stack.pop()
        for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nh = h + dy
            nw = w + dx
            if 0 <= nh < H and 0 <= nw < W and (dp[nh][nw] == -1 or dp[nh][nw] > dp[h][w]):
                if cell[nh][nw] == '.':
                    dp[nh][nw] = dp[h][w]
                    stack.append([nh,nw])
                    copy_stack.append([nh,nw])
                   
while True:
    if len(copy_stack):
        nstack = copy.copy(copy_stack)
    else:
        copy_stack = copy.copy(nstack)
    search(nstack)
    #魔法による５*５の移動
    if dp[Dh][Dw] == -1:
        while len(copy_stack)>0:
            h,w = copy_stack.pop()
            for ddy in range(-2,3):
                for ddx in range(-2,3):
                    if ddy==ddx==0:
                        continue
                    nnh = h + ddy
                    nnw = w + ddx
                    if 0 <= nnh < H and 0 <= nnw < W:
                        if cell[nnh][nnw] == '.' and dp[nnh][nnw] == -1:
                            dp[nnh][nnw] = dp[h][w] + 1
                            nstack.append([nnh,nnw])
        if len(nstack) == 0:
            break
    else:
        break
                        
if dp[Dh][Dw] != -1:
    print(dp[Dh][Dw])
else:
    print(-1)
