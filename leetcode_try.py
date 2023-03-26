from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


from collections import deque


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        m = len(queries)
        ans = []
        max_val = max(nums)

        # 事前に最大値と最小値を計算しておく
        min_val = min(nums)
        diff = max_val - min_val

        # 差分配列を作成
        diff_arr = [0] * (diff + 1)
        for i in range(n):
            diff_arr[nums[i] - min_val] += 1

        # クエリーごとに最小の操作回数を計算
        for q in queries:
            if q < min_val:
                ans.append(n * (min_val - q))
            elif q > max_val:
                ans.append(n * (q - max_val))
            else:
                ans.append(
                    sum(diff_arr[q - min_val + 1 :])
                    + (n - sum(diff_arr[: q - min_val]))
                )

        return ans


S = Solution()

nums = [3, 1, 6, 8]
queries = [1, 5]
print(S.minOperations(nums, queries))
