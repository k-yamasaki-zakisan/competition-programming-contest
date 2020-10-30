# https://leetcode.com/problems/longest-common-prefix/

class Solution:
   def longestCommonPrefix(self, strs: list) -> str:
        ans = strs[0]
        for i in range(1,len(strs)):
            cdd = strs[i]
            tmp_l = min(len(ans),len(cdd))
            f_flag = True
            while 0 < tmp_l:
                if ans[:tmp_l] == cdd[:tmp_l]:
                    ans = ans[:tmp_l]
                    f_flag = False
                    break
                tmp_l -= 1
            if f_flag:
                return ""
        return ans