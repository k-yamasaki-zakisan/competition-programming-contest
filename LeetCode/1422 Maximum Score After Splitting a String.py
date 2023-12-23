class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(1, n):
            left, right = s[:i], s[i:]
            tmp_score = len([l for l in left if l == "0"]) + len(
                [r for r in right if r == "1"]
            )
            ans = max(ans, tmp_score)
        return ans
