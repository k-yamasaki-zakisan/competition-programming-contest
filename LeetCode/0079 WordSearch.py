# https://leetcode.com/problems/word-search/
# Runtime: 380 ms, faster than 41.53% of Python3 online submissions for Word Search.
# Memory Usage: 15.6 MB, less than 5.32% of Python3 online submissions for Word Search.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dps(h,w,count,root,ans):
            if ans == True:
                return ans
            if count == len(word):
                ans = True
                return ans
            for ry,rx in [[1,0],[0,1],[-1,0],[0,-1]]:
                ny, nx = h+ry, w+rx
                if 0 <= ny < H and 0 <= nx < W and root[ny][nx] == 0:
                    root[ny][nx] = 1
                    if board[ny][nx] == word[count]:
                        count += 1
                        ans = dps(ny,nx,count,root,ans)
                        count -= 1
                    root[ny][nx] = 0
            return ans

        H = len(board)
        W = len(board[0])
        for h in range(H):
            for w in range(W):
                if board[h][w] == word[0]:
                    root = [[0]*W for _ in range(H)]
                    root[h][w] = 1
                    count = 1
                    ans = False
                    result = dps(h,w,count,root,ans)
                    if result:
                        return True
        return False