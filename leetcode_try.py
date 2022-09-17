from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        from collections import defaultdict

        cnt = defaultdict(int)
        for ma in matrix:
            cnt[tuple(ma)] += 1
            re_ma = tuple([(m + 1) % 2 for m in ma])
            cnt[re_ma] += 1
        return max(cnt.values())


S = Solution()
matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(S.maxEqualRowsAfterFlips(matrix))
