from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        dp = [[0, 0]]
        if nums[0] == 0:
            dp[-1][0] += 1
        else:
            dp[-1][-1] += 1
        for i in range(1, len(nums)):
            num = nums[i]
            tmp = [0, 0]
            if num == 0:
                tmp[0] = dp[-1][-1] + 1
            else:
                tmp[-1] = dp[-1][0] + 1
            dp.append(tmp)
        return sum([sum(d) for d in dp])
