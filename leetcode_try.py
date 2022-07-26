from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(str(int("".join([str(n) for n in num])) + k))


num = [1, 2, 0, 0]
k = 34
S = Solution()
print(S.addToArrayForm(num, k))
