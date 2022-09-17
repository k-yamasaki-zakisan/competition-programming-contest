# https://leetcode.com/problems/distant-barcodes/
# Runtime: 452 ms, faster than 95.30% of Python3 online submissions for Distant Barcodes.
# Memory Usage: 16.3 MB, less than 68.78% of Python3 online submissions for Distant Barcodes.

from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter

        cnt_b = Counter(barcodes)
        cnt_b = [[key, val] for key, val in cnt_b.items()]
        cnt_b = sorted(cnt_b, key=lambda x: x[1])
        len_b = len(barcodes)
        ans = [-1] * len_b
        for i in range(0, len_b, 2):
            ans[i] = cnt_b[-1][0]
            cnt_b[-1][1] -= 1
            if not cnt_b[-1][1]:
                cnt_b.pop()
        for i in range(1, len_b, 2):
            ans[i] = cnt_b[-1][0]
            cnt_b[-1][1] -= 1
            if not cnt_b[-1][1]:
                cnt_b.pop()
        return ans
