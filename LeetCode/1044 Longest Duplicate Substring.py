# https://leetcode.com/problems/longest-duplicate-substring/
# Runtime: 4065 ms, faster than 45.13% of Python3 online submissions for Longest Duplicate Substring.
# Memory Usage: 14.3 MB, less than 97.92% of Python3 online submissions for Longest Duplicate Substring.


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        cnt = 0
        ans = ""
        len_s = len(s)
        for i in range(len_s):
            if len_s <= i + cnt:
                break
            ss = s[i : i + cnt + 1]
            sentence = s[i + 1 :]
            while i + cnt < len_s and ss in sentence:
                cnt += 1
                ans = ss
                ss += s[i + cnt]
        return ans
