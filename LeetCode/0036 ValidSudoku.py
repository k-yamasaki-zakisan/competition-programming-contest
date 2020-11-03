# https://leetcode.com/problems/valid-sudoku/
# Runtime: 100 ms, faster than 51.42% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 横判定
        for i in range(9):
            tmp_s = set()
            tmp_l = []
            b = board[i]
            for j in range(9):
                if b[j] != '.':
                    tmp_s.add(b[j])
                    tmp_l.append(b[j])
            if len(list(tmp_s)) != len(tmp_l):
                return False
        # 縦判定
        for i in range(9):
            tmp_s = set()
            tmp_l = []
            for j in range(9):
                if board[j][i] != '.':
                    tmp_s.add(board[j][i])
                    tmp_l.append(board[j][i])
            if len(list(tmp_s)) != len(tmp_l):
                return False
        # 3*3の判定
        for i in range(3):
            for p in range(3):
                rng_t = i*3
                rng_s = p*3
                tmp_s = set()
                tmp_l = []
                for j in range(rng_t,rng_t+3):
                    for k in range(rng_s,rng_s+3):
                        if board[j][k] != ".":
                            tmp_s.add(board[j][k])
                            tmp_l.append(board[j][k])
                if len(list(tmp_s)) != len(tmp_l):
                    return False
        return True