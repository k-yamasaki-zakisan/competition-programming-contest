from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        nums = sorted([a, b, c])
        print(nums)


S = Solution()
a = 1
b = 20
c = 5
print(S.numMovesStones(a, b, c))
