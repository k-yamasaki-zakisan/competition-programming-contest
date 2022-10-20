from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        i_0, i_1, i_2 = 0, 1, 1
        for _ in range(n - 2):
            i_0, i_1, i_2 = i_1, i_2, i_0 + i_1 + i_2
        return i_2


S = Solution()
n = 25
print(S.tribonacci(n))
