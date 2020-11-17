# https://atcoder.jp/contests/past202005-open/tasks/past202005_g

from collections import deque

N,X,Y = map(int,input().split())
X,Y = X+250, Y+250
XY = [list(map(int,input().split())) for _ in range(N)]
root = [['.']*500 for _ in range(500)]
for x,y in XY:
    x,y = x+250,y+250
    root[y][x] = '#'

stack = deque([[250,250]])
check = [[-1]*500 for _ in range(500)]
check[250][250] = 0
while len(stack):
    h,w = stack.popleft()
    for x,y in [[1,0],[0,1],[-1,1],[-1,0],[0,-1],[1,1]]:
        nh,nw = h+y,w+x
        if 0<=nh<500 and 0<=nw<500 and root[nh][nw] == '.' and check[nh][nw] == -1:
            check[nh][nw] = check[h][w]+1
            stack.append([nh,nw])
            if nh == Y and nw == X:
                print(check[nh][nw])
                exit()
print(-1)