# https://leetcode.com/problems/longest-common-prefix/
# Runtime: 32 ms, faster than 77.26% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.

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