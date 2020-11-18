# https://atcoder.jp/contests/abc037/tasks/abc037_d

import sys
sys.setrecursionlimit(1000000)
mod = 10**9+7
move = [[1,0],[-1,0],[0,-1],[0,1]]

def dps(y:int,x:int) -> int:
    if ans[y][x] != 1:
        return ans[y][x]
    for dy,dx in move:
        ny,nx = y+dy,x+dx
        if  0<=ny<H and 0<=nx<W:
            if A[y][x] < A[ny][nx]:
                ans[y][x] += dps(ny,nx)
    ans[y][x]%=mod
    return ans[y][x]

H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
ans = [[1]*W for _ in range(H)]
for h in range(H):
    for w in range(W):
        dps(h,w)

print(sum([sum(x)for x in ans])%mod)