# https://leetcode.com/problems/long-pressed-name/
# Runtime: 12 ms, faster than 100.00% of Python3 online submissions for Long Pressed Name.
# Memory Usage: 14.1 MB, less than 86.04% of Python3 online submissions for Long Pressed Name.


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l_n = len(name)
        i = 0
        for j in range(len(typed)):
            if i < l_n and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == l_n
