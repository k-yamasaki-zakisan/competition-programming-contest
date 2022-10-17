from typing import List, Optional

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        for t_num in range(num + 1):
            rev_t_num = int(str(t_num)[::-1])
            if t_num + rev_t_num == num:
                return True
        return False


S = Solution()
n = 0
print(S.sumOfNumberAndReverse(n))
