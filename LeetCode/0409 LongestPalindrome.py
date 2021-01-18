# https://leetcode.com/problems/longest-palindrome/
# Runtime: 20 ms, faster than 99.51% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 14.1 MB, less than 80.59% of Python3 online submissions for Longest Palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        for ss in s:
            memo[ss] += 1
        ans = 0
        for val in memo.values():
            if val % 2:
                ans += 1
                break
        for val in memo.values():
            ans += (val//2)*2
        return ans
