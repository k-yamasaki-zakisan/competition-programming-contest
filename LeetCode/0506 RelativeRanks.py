# https://leetcode.com/problems/relative-ranks/
# Runtime: 64 ms, faster than 91.70% of Python3 online submissions for Relative Ranks.
# Memory Usage: 15.3 MB, less than 41.70% of Python3 online submissions for Relative Ranks.

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        from collections import defaultdict
        nums_sort = sorted(nums)[::-1]
        nums_dict = defaultdict(str)
        for i, num in enumerate(nums_sort):
            i += 1
            if i == 1:
                nums_dict[num] = 'Gold Medal'
            elif i == 2:
                nums_dict[num] = 'Silver Medal'
            elif i == 3:
                nums_dict[num] = 'Bronze Medal'
            else:
                nums_dict[num] = str(i)
        ans = []
        for num in nums:
            ans.append(nums_dict[num])
        return ans
