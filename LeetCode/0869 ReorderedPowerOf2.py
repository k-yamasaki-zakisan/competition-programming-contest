# https://leetcode.com/problems/reordered-power-of-2/
# Runtime: 28 ms, faster than 94.63% of Python3 online submissions for Reordered Power of 2.
# Memory Usage: 14.2 MB, less than 82.93% of Python3 online submissions for Reordered Power of 2.

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import defaultdict
        if n == 1:
            return True
        len_n = len(str(n))
        n_nums = [0]*10
        for nn in str(n):
            n_nums[int(nn)] += 1
        base = 1
        cands = []
        while len(str(base*2)) <= len_n:
            if len(str(base*2)) == len_n:
                cands.append(base*2)
            base *= 2
        for num in cands:
            tmp = [0]*10
            for numm in str(num):
                tmp[int(numm)] += 1
            if n_nums == tmp:
                return True
        return False