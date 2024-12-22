from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        max_index = 0
        for i in range(len(arr)):
            max_index = max(max_index, arr[i])
            if max_index == i:
                ans += 1
                max_index += 1
        return ans
