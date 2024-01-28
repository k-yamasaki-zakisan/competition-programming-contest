from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)
        nums_set = set(nums)
        ans = 1
        for num in nums_set:
            if num == 1:
                ans = max(ans, nums_cnt[1] if nums_cnt[1] % 2 else nums_cnt[1] - 1)
                continue
            if nums_cnt[num] < 2:
                continue
            next_num = num**2
            tmp_cnt = 2
            while 0 < nums_cnt[next_num]:
                ans = max(ans, tmp_cnt + 1)
                if nums_cnt[next_num] == 1:
                    break
                next_num = next_num**2
                tmp_cnt += 2
        return ans
