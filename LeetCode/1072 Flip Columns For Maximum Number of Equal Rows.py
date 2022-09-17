# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
# Runtime: 1643 ms, faster than 88.29% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
# Memory Usage: 16.4 MB, less than 19.82% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.

from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        for ma in matrix:
            cnt[tuple(ma)] += 1
            re_ma = tuple([(m + 1) % 2 for m in ma])
            cnt[re_ma] += 1
        return max(cnt.values())
