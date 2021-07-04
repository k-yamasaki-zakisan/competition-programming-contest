# https://leetcode.com/problems/shifting-letters/
# Runtime: 184 ms, faster than 71.88% of Python3 online submissions for Shifting Letters.
# Memory Usage: 17.3 MB, less than 45.21% of Python3 online submissions for Shifting Letters.

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        sum_shifts = [0]*len(S)
        tmp_num = sum(shifts)
        for i, shift in enumerate(shifts):
            sum_shifts[i] = tmp_num
            tmp_num -= shift

        ans = ''
        base_ord = ord('a')
        for i in range(len(S)):
            s = S[i]
            shift = sum_shifts[i] % 26
            word = chr((ord(s)-base_ord+shift) % 26+base_ord)
            ans += word
        return ans
