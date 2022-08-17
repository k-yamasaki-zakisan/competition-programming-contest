from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False
        base = sum_arr // 3
        tmp = 0
        cnt = 0
        print(base)
        for a in arr:
            tmp += a
            if tmp == base:
                cnt += 1
                tmp = 0
            if cnt == 3:
                return True
            print(a, tmp, cnt)
        return False


n = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
S = Solution()
print(S.canThreePartsEqualSum(n))
