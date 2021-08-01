# https://leetcode.com/problems/lemonade-change/
# Runtime: 820 ms, faster than 13.74% of Python3 online submissions for Lemonade Change.
# Memory Usage: 18.1 MB, less than 15.37% of Python3 online submissions for Lemonade Change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        coins = [0]*3
        for bill in bills:
            if bill == 5:
                coins[0] += 1
            elif bill == 10:
                coins[1] += 1
                if coins[0]:
                    coins[0] -= 1
                else:
                    return False
            else:
                coins[2] += 1
                if coins[0] and coins[1]:
                    coins[0] -= 1
                    coins[1] -= 1
                elif 3 <= coins[0]:
                    coins[0] -= 3
                else:
                    return False
        return True