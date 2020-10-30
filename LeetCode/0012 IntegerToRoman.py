# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        trans = {
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        num = list(str(num))
        len_n = len(num)-1
        ans = ''
        for n in num:
            n = int(n)
            keta = 10**len_n
            if n == 0:
                pass
            elif n == 5:
                ans = ans + trans[n*keta]
            elif n == 4:
                ans = ans + trans[keta] + trans[5*keta]
            elif n == 9:
                ans = ans + trans[keta] + trans[10*keta]
            elif 0 < n < 4:
                ans = ans + trans[keta]*n
            else:
                ans = ans + trans[keta*5] + trans[keta]*(n-5)
            len_n -= 1
        return ans