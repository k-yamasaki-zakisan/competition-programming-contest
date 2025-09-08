from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            if "0" in str(a):
                continue
            if "0" in str(n - a):
                continue
            return [a, n - a]
