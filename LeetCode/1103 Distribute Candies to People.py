# https://leetcode.com/problems/distribute-candies-to-people/
# Runtime: 97 ms, faster than 10.88% of Python3 online submissions for Distribute Candies to People.
# Memory Usage: 13.9 MB, less than 88.70% of Python3 online submissions for Distribute Candies to People.

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cnt = 1
        ans = [0] * num_people
        i = 0
        while 0 < candies:
            ans[i] += min(cnt, candies)
            candies -= cnt
            if candies <= 0:
                break
            cnt += 1
            i = (i + 1) % num_people
        return ans
