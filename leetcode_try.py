from typing import List, Optional

from numpy import s_

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans, tmp = 0, 0
        memo = {}
        for i in range(len(hours)):
            tmp += 1 if 8 < hours[i] else -1
            if 0 < tmp:
                ans = i + 1
            else:
                if tmp not in memo:
                    memo[tmp] = i
                if tmp - 1 in memo:
                    ans = max(ans, i - memo[tmp - 1])
        return ans


S = Solution()
hours = [6, 6, 8]
print(S.longestWPI(hours))
