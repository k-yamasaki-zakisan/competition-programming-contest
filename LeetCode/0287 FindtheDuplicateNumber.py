# https://leetcode.com/problems/find-the-duplicate-number/
# Runtime: 68 ms, faster than 46.36% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 18.4 MB, less than 12.27% of Python3 online submissions for Find the Duplicate Number.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
