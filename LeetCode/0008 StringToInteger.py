# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        MAXV = 2147483648
        h_cdd = ['1','2','3','4','5','6','7','8','9']
        cdd = ['0','1','2','3','4','5','6','7','8','9']
        new_s = s.strip().split()
        if len(new_s) == 0:
            return 0
        new_s = new_s[0]
        new_s = list(new_s)
        if len(new_s) == 1:
            if new_s[0] in h_cdd:
                return int(new_s[0])
            else:
                return 0
        else:
            if new_s[0] == '-':
                ans = '-'
                new_s.pop(0)
            elif new_s[0] == '+':
                ans = ''
                new_s.pop(0)
            else:
                ans = ''
        
        while len(new_s) and new_s[0] == "0":
            new_s.pop(0)
        if len(new_s):
            if new_s[0] in h_cdd:
                ans = ans + new_s[0]
            else:
                return 0
        else:
            return 0
        
        i = 1
        while i < len(new_s):
            if new_s[i] in cdd:
                ans = ans+new_s[i]
                i += 1
            #elif new_s[i] == '.':
            #    break
            else:
                break
        ans = int(ans)
        if ans<-MAXV:
            return -MAXV
        elif MAXV-1<ans:
                return MAXV-1
        else:
            return ans