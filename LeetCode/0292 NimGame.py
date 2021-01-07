# https://leetcode.com/problems/nim-game/
# Runtime: 32 ms, faster than 42.80% of Python3 online submissions for Nim Game.
# Memory Usage: 14 MB, less than 86.97% of Python3 online submissions for Nim Game.

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        else:
            return True
