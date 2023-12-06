from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while 0 < n:
            print(n)
            ans += (n + 1) // 2
            n = (n + 1) // 2
        return ans


S = Solution()
a = 0
b = 3
n = 1
print(S.maximumXorProduct(a, b, n))
# 10
