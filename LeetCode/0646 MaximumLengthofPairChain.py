# https://leetcode.com/problems/maximum-length-of-pair-chain/
# Runtime: 188 ms, faster than 99.64% of Python3 online submissions for Maximum Length of Pair Chain.
# Memory Usage: 14.8 MB, less than 65.63% of Python3 online submissions for Maximum Length of Pair Chain.

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sort_pairs = sorted(pairs, key=lambda x: x[1])
        ans = 1
        tail = sort_pairs[0][1]
        for i in range(1, len(sort_pairs)):
            if tail < sort_pairs[i][0]:
                tail = sort_pairs[i][1]
                ans += 1
        return ans
