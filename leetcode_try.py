from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


from collections import deque


class Solution:
    def minCost(self, nums: List[int], k: int):
        from collections import defaultdict
        import copy

        len_nums = len(nums)
        dp = [[defaultdict(int) for _ in range(len_nums)] for _ in range(len_nums)]
        for i, num in enumerate(nums):
            for j in range(i + 1):
                if j < i:
                    dp[i][j] = copy.deepcopy(dp[i - 1][j])
                if j == i:
                    dp[i][j][num] += 1
                dp[j][j][num] += 1
        for d in dp:
            print(d)


S = Solution()

nums = [1, 2, 1, 2, 1]
k = 2
print(S.minCost(nums, k))
