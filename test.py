from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        import math
        import itertools

        points = set(map(tuple, points))

        def vector_len(a):
            return math.sqrt(a[0] ** 2 + a[1] ** 2)

        ans = float("inf")
        for p1, p2, p3 in itertools.permutations(points, 3):
            p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
            if p4 in points:
                v21 = (p2[0] - p1[0], p2[1] - p1[1])
                v31 = (p3[0] - p1[0], p3[1] - p1[1])
                if abs(v21[0] * v31[0] + v21[1] * v31[1]) == 0:
                    area = vector_len(v21) * vector_len(v31)
                    ans = min(ans, area)

        return ans if ans < float("inf") else 0


points = [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]
S = Solution()
print(S.minAreaFreeRect(points))
