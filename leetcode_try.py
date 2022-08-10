from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def clumsy(self, n: int) -> int:
        nums = [num for num in range(n, 0, -1)]
        minus = []
        plus = []
        minus_num = 1
        for i in range(n):
            if i % 4 == 0 or i % 4 == 1:
                minus_num *= nums[i]
            elif i % 4 == 2:
                minus_num //= nums[i]
                minus.append(minus_num)
                minus_num = 1
            else:
                plus.append(nums[i])
        if n % 4 == 1 or n % 4 == 2:
            minus.append(minus_num)
        ans = minus[0] + sum(plus)
        print(minus, plus, minus_num)
        for i in range(1, len(minus)):
            ans -= minus[i]
        return ans


n = 5
S = Solution()
print(S.clumsy(n))
