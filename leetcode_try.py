from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = [[x**2 + y**2, x, y] for x, y in points]
        ans = sorted(ans, key=lambda x: x[0])
        return [[x, y] for p, x, y in ans[:k]]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
S = Solution()
print(S.kClosest(points, k))
