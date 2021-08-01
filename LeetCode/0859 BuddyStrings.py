# https://leetcode.com/problems/buddy-strings/
# Runtime: 36 ms, faster than 51.81% of Python3 online submissions for Buddy Strings.
# Memory Usage: 14.5 MB, less than 43.54% of Python3 online submissions for Buddy Strings.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        s_len, goal_len = len(s), len(goal)
        diff = []
        for i in range(s_len):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
        if len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]:
            return True
        elif len(diff) == 0 and s_len != len(set(s)):
            return True
        return False