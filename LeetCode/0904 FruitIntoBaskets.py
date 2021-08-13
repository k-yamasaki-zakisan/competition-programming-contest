# https://leetcode.com/problems/fruit-into-baskets/
# Runtime: 844 ms, faster than 44.95% of Python3 online submissions for Fruit Into Baskets.
# Memory Usage: 20.1 MB, less than 69.85% of Python3 online submissions for Fruit Into Baskets.


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        memo = defaultdict(int)
        kind = tail = ans = 0
        for i in range(len(fruits)):
            memo[fruits[i]] += 1
            if memo[fruits[i]] == 1:
                kind += 1
            while 2 < kind:
                memo[fruits[tail]] -= 1
                if memo[fruits[tail]] == 0:
                    kind -= 1
                tail += 1
            ans = max(ans, i-tail+1)
        return ans
