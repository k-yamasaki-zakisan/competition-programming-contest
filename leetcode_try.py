from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        import math

        L = list(map(int, str(N + 1)))
        print(L)
        res = sum(9 * perm(9, i) for i in range(n - 1))
        print(res)


n = 1000
S = Solution()
print(S.numDupDigitsAtMostN(n))
