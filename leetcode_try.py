from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        words = text.split(" ")
        ans = [
            words[i + 1]
            for i in range(1, len(words) - 1)
            if (words[i - 1] == first and words[i] == second)
        ]
        return ans


S = Solution()
matrix = [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
print(S.maxEqualRowsAfterFlips(matrix))
