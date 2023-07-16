from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter

        n = len(nums)
        cnt = sorted(list(Counter(nums).items()), key=lambda x: -x[1])
        f, l, target = 0, cnt[0][1], cnt[0][0]
        for i in range(n):
            if target == nums[i]:
                f += 1
                l -= 1
            if i + 1 < f * 2 and n - i - 1 < l * 2:
                return i
        return -1
