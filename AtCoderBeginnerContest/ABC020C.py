# https://atcoder.jp/contests/abc020/tasks/abc020_c

from heapq import *

def judge(m):
    dist = [[10**18]*W for _ in range(H)]
    dist[sy][sx] = 0
    step = []
    heappush(step, (dist[sy][sx], sy, sx))

    while len(step):
        d,y,x = heappop(step)
        if dist[y][x]>d:
            continue
        for cy,cx in [[1,0],[-1,0],[0,1],[0,-1]]:
            nh,nw = y+cy, x+cx
            if not (0<=nh<H and 0<=nw<W):
                continue
            if dist[nh][nw]>dist[y][x]+(m if S[nh][nw]=='#' else 1):
                dist[nh][nw] = dist[y][x]+(m if S[nh][nw]=='#' else 1)
                heappush(step, (dist[nh][nw], nh, nw))
    return dist[gy][gx]<=T


H,W,T = map(int,input().split())
S = [list(input()) for _ in range(H)]
start = []
goal = []
for h in range(H):
    for w in range(W):
        if S[h][w] == "S":
            sy,sx = h,w
        elif S[h][w] == "G":
            gy,gx = h,w

l, r = 0, 10**9
while 1 < abs(r-l):
    mid = (l+r)//2
    if judge(mid):
        l = mid
    else:
        r = mid
print(l)