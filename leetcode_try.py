from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        memo = []
        len_arr = len(arr)
        for i in range(len_arr - 1):
            if arr[i] < arr[i + 1]:
                memo.append("<")
            elif arr[i] > arr[i + 1]:
                memo.append(">")
            else:
                memo.append("=")
        ans = 1
        cnt = 1
        for i in range(1, len(memo)):
            if (memo[i - 1] == "<" and memo[i] == ">") or (
                memo[i - 1] == ">" and memo[i] == "<"
            ):
                cnt += 1
            else:
                ans = max(ans, cnt + 1)
                cnt = 1
            # print(i, cnt)
        return max(ans, cnt + 1)


arr = [0, 8, 45, 88, 48, 68, 28, 55, 17, 24]
S = Solution()
print(S.maxTurbulenceSize(arr))
