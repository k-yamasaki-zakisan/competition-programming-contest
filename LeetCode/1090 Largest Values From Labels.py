# https://leetcode.com/problems/largest-values-from-labels/
# Runtime: 167 ms, faster than 83.16% of Python3 online submissions for Largest Values From Labels.
# Memory Usage: 19.3 MB, less than 31.23% of Python3 online submissions for Largest Values From Labels.

from typing import List


class Solution:
    def largestValsFromLabels(
        self, values: List[int], labels: List[int], numWanted: int, useLimit: int
    ) -> int:
        from collections import defaultdict

        cnt = ans = 0
        zip_vals = sorted(zip(values, labels), key=lambda x: -x[0])
        use_memo = defaultdict(int)
        for val, label in zip_vals:
            if use_memo[label] < useLimit:
                cnt += 1
                ans += val
                use_memo[label] += 1
            if cnt == numWanted:
                break
        return ans
