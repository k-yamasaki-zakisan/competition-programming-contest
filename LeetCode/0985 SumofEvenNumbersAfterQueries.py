# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# Runtime: 667 ms, faster than 64.57% of Python3 online submissions for Sum of Even Numbers After Queries.
# Memory Usage: 20.4 MB, less than 78.37% of Python3 online submissions for Sum of Even Numbers After Queries.

from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        result = sum([num for num in nums if num % 2 == 0])
        ans = []
        for query in queries:
            val, index = query
            if nums[index] % 2 == 0:
                result -= nums[index]
            if (nums[index] + val) % 2 == 0:
                result += nums[index] + val
            nums[index] += val
            ans.append(result)
        return ans
