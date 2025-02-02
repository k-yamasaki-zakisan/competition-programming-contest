from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            flag = True
            for j in range(n - 1):
                if not (nums[(i + j) % n] <= nums[(i + j + 1) % n]):
                    flag = False
                    break
            if flag:
                return True
        return False
