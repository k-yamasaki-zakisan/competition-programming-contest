#https://atcoder.jp/contests/agc033/tasks/agc033_a

from collections import deque
 
H, W = [int(x) for x in input().split()]
cell = [list(input()) for i in range(H)]
 
painted = deque()
for h in range(H):
    for w in range(W):
        if cell[h][w] == '#':
            painted.append([h, w, 0])
 
ans = 0
while len(painted) > 0:
    blackcell = painted.popleft()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nh = blackcell[0] + dy
        nw = blackcell[1] + dx
        d = blackcell[2]
        if 0 <= nh < H and 0 <= nw < W and cell[nh][nw] == '.':
            cell[nh][nw] = '#'
            painted.append([nh, nw, d + 1])
        ans = d
 
print(ans)
