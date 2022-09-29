from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cnt = 1
        ans = [0] * num_people
        for i in range(candies):
            i %= num_people
            ans[i] += min(cnt, candies)
            candies -= cnt
            if candies <= 0:
                break
            cnt += 1
        return ans


S = Solution()
candies = 10
num_people = 3
print(S.distributeCandies(candies, num_people))
