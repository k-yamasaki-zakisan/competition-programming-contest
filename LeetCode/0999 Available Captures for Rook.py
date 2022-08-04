# https://leetcode.com/problems/available-captures-for-rook/
# Runtime: 42 ms, faster than 73.26% of Python3 online submissions for Available Captures for Rook.
# Memory Usage: 14 MB, less than 37.17% of Python3 online submissions for Available Captures for Rook.

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt = 0
        H = len(board)
        W = len(board[0])
        for h in range(H):
            for w in range(W):
                if board[h][w] == "R":
                    nnh, nnw = h, w
                    break
        for y, x in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh, nw = nnh, nnw
            while True:
                neh, new = nh + y, nw + x
                if 0 <= neh < H and 0 <= new < W and board[neh][new] != "B":
                    if board[neh][new] == "p":
                        cnt += 1
                        break
                    else:
                        nh, nw = neh, new
                else:
                    break
        return cnt
