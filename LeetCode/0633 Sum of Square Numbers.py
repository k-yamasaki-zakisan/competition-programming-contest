class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        memo = set()
        while i**2 <= c:
            memo.add(i**2)
            i += 1
        for m in memo:
            if c - m in memo:
                return True
        return False
