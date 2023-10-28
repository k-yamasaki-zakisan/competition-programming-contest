class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                continue
            tmp = s[i] + s[i + 1]
            if len(ans) == 1:
                ans = tmp
            for j in range(1, min(i + 1, n - i - 1)):
                if s[i - j] == s[i + 1 + j]:
                    tmp = s[i - j] + tmp + s[i + 1 + j]
                else:
                    break
            if len(ans) < len(tmp):
                ans = tmp
        for i in range(1, n):
            tmp = s[i]
            for j in range(1, min(i, n - i - 1) + 1):
                if s[i - j] == s[i + j]:
                    tmp = s[i - j] + tmp + s[i + j]
                else:
                    break
            if len(ans) < len(tmp):
                ans = tmp
        return ans
