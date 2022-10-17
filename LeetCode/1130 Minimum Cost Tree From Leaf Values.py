# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
# Runtime: 64 ms, faster than 62.67% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
# Memory Usage: 14 MB, less than 47.74% of Python3 online submissions for Minimum Cost Tree From Leaf Values.

from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        ans = 0
        while 1 < len(arr):
            i = arr.index(min(arr))
            if i != 0 and i != len(arr) - 1:
                ans += arr[i] * min(arr[i - 1], arr[i + 1])
            elif i == 0:
                ans += arr[i] * arr[1]
            else:
                ans += arr[i] * arr[i - 1]
            arr.pop(i)
        return ans
