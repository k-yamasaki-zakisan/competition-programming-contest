from typing import List
from collections import Counter


class Solution:
    def earliestSecondToMarkIndices(
        self, nums: List[int], changeIndices: List[int]
    ) -> int:
        n, m = len(nums), len(changeIndices)
        for seconds in range(len(changeIndices) + 1):
            change_indices = changeIndices[:seconds]
            remaining, can_decrement = Counter(change_indices), 0
            marked = set()

            for i in change_indices:
                if remaining[i] == 1 and i not in marked:
                    if nums[i - 1] - can_decrement <= 0:
                        marked.add(i)
                        can_decrement -= nums[i - 1]
                    else:
                        break
                else:
                    remaining[i] -= 1
                    can_decrement += 1

            if len(marked) == n:
                return seconds
        return -1
