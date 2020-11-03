# https://leetcode.com/problems/implement-strstr/
# Runtime: 28 ms, faster than 83.58% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.2 MB, less than 8.04% of Python3 online submissions for Implement strStr().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
