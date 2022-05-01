from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import defaultdict

        plus, minus, zero_cnt = defaultdict(int), defaultdict(int), 0
        plus_num, minus_num = [], []
        for a in arr:
            if 0 < a:
                plus[a] += 1
                plus_num.append(a)
            elif 0 == a:
                zero_cnt += 1
            else:
                minus[abs(a)] += 1
                minus_num.append(abs(a))
        if zero_cnt % 2:
            return False

        plus_num.sort()
        for num in plus_num:
            if 0 < plus[num]:
                if plus[num] <= plus[num * 2]:
                    plus[num * 2] -= plus[num]
                    plus[num] = 0
                else:
                    return False
        minus_num.sort()
        for num in minus_num:
            if 0 < minus[num]:
                if minus[num] <= minus[num * 2]:
                    minus[num * 2] -= minus[num]
                    minus[num] = 0
                else:
                    return False
        return True


arr = [4, -2, 2, -4]
S = Solution()
print(S.canReorderDoubled(arr))
