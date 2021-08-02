# https://leetcode.com/problems/binary-gap/
# Runtime: 28 ms, faster than 84.74% of Python3 online submissions for Binary Gap.
# Memory Usage: 14.3 MB, less than 46.51% of Python3 online submissions for Binary Gap.

class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)
        head = -1
        tmp = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                if head != -1:
                    tmp =  max(i-head, tmp)
                head = i
        return tmp