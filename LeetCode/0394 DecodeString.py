# https://leetcode.com/problems/decode-string/
# Runtime: 28 ms, faster than 76.53% of Python3 online submissions for Decode String.
# Memory Usage: 14.1 MB, less than 87.65% of Python3 online submissions for Decode String.

class Solution:
    def decodeString(self, s: str) -> str:
        is_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        change = True
        while change:
            change = False
            left_kako = -1
            for i, ss in enumerate(s):
                if ss == '[':
                    left_kako = i
                    num_i = left_kako-1
                    num = ''
                    while 0 <= num_i and s[num_i] in is_num:
                        num = s[num_i]+num
                        num_i -= 1
                    num_i += 1
                elif left_kako != -1 and ss == ']':
                    tmp_s = s[:num_i] + \
                        int(num)*s[left_kako+1:i]+s[i+1:]
                    change = True
                    break
            if change:
                s = tmp_s
        return s
