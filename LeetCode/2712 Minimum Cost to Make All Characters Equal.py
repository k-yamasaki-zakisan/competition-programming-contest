class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n - 1):
            if s[i] != s[i + 1]:
                ans += min(i + 1, n - i - 1)
        return ans
