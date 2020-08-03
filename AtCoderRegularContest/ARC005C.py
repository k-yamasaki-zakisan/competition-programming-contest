#https://atcoder.jp/contests/arc005/tasks/arc005_3

from collections import deque
 
H, W = [int(x) for x in input().split()]
root = [list(input()) for i in range(H)]
dp = [[10000000 for i in range(W)] for j in range(H)]
step = deque()
for h in range(H):
    for w in range(W):
        if root[h][w] == 's':
            step.append([h, w])
            dp[h][w] = 0
 
while len(step) > 0:
    h,w = step.popleft()
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nh = h + dy
        nw = w + dx
        if 0 <= nh < H and 0 <= nw < W:
            if root[nh][nw] == 'g':
                print('YES')
                exit()
            elif root[nh][nw] == '.':
                if dp[h][w] < dp[nh][nw]:
                    step.append([nh, nw])
                    dp[nh][nw] = dp[h][w]
            elif root[nh][nw] == '#':
                if dp[h][w] < 2 and dp[h][w]+1 < dp[nh][nw]:
                    step.append([nh, nw])
                    dp[nh][nw] = dp[h][w]+1
        #print(dp[0])
print('NO')
