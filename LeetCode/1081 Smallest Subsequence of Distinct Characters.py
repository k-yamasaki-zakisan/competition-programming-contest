# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Runtime: 29 ms, faster than 99.01% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
# Memory Usage: 14 MB, less than 18.89% of Python3 online submissions for Smallest Subsequence of Distinct Characters.


class Solution:
    def smallestSubsequence(self, S: str) -> str:
        last_points = {s: i for i, s in enumerate(S)}
        ans = []
        for i, s in enumerate(S):
            if s in ans:
                continue

            while ans and s < ans[-1] and i < last_points[ans[-1]]:
                ans.pop()
            ans.append(s)
        return "".join(ans)
