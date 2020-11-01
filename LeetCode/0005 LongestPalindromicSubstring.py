# https://leetcode.com/problems/longest-palindromic-substring/
# Runtime: 1468 ms, faster than 46.96% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 14.2 MB, less than 9.26% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s[0]
        ans = s[1]
        for i in range(1,len(s)-1):
            tmp_cnt = 0
            while 0 <= i-(tmp_cnt+1) and i+(tmp_cnt+1) <= len(s)-1:
                if s[i-(tmp_cnt+1)] == s[i+(tmp_cnt+1)]:
                    tmp_cnt += 1
                else:
                    break
            if len(ans) < tmp_cnt*2+1:
                ans = s[i-(tmp_cnt):i+tmp_cnt+1]
        for i in range(len(s)-1):
            tmp_cnt = 0
            while 0 <= i-(tmp_cnt) and i+(tmp_cnt+1) <= len(s)-1:
                if s[i-tmp_cnt] == s[i+tmp_cnt+1]:
                    tmp_cnt += 1
                else:
                    break
            if len(ans) < tmp_cnt*2:
                ans = s[i-(tmp_cnt-1):i+tmp_cnt+1]
        return ans