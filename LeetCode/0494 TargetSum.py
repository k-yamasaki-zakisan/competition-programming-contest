# https://leetcode.com/problems/target-sum/
# Runtime: 264 ms, faster than 68.21% of Python3 online submissions for Target Sum.
# Memory Usage: 14.3 MB, less than 88.27% of Python3 online submissions for Target Sum.

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        from collections import Counter
        queue = Counter([0])
        for num in nums:
            new_n = Counter()
            for k, v in queue.items():
                new_n[k-num] += v
                new_n[k+num] += v

            queue = new_n

        return queue[S]
