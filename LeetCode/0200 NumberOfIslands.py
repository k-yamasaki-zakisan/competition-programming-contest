# https://leetcode.com/problems/number-of-islands/
# Runtime: 140 ms, faster than 61.46% of Python3 online submissions for Number of Islands.
# Memory Usage: 15.4 MB, less than 32.27% of Python3 online submissions for Number of Islands.

from collections import deque
        ans = 0
        H = len(grid)
        W = len(grid[0])
        check = [[0]*W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w] == '1' and check[h][w] == 0:
                    ans += 1
                    stack = deque([[h,w]])
                    check[h][w] = 1
                    while len(stack):
                        y,x = stack.popleft()
                        for n_h, n_w in [[1,0],[-1,0],[0,1],[0,-1]]:
                            nh,nw = y+n_h,x+n_w
                            if 0<=nh<H and 0<=nw<W:
                                if grid[nh][nw] == '1' and check[nh][nw] == 0:
                                    check[nh][nw] = 1
                                    stack.append([nh,nw])
        return ans