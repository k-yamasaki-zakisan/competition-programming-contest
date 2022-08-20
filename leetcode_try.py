from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        bin_n = bin(n)[2:]
        print(bin_n)
        return bin_n in s


n = "110101011011000011011111000000"
s = 15

S = Solution()
print(S.queryString(n, s))
