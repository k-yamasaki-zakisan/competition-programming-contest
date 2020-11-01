# https://leetcode.com/problems/zigzag-conversion/
# Runtime: 56 ms, faster than 77.16% of Python3 online submissions for ZigZag Conversion.
# Memory Usage: 14.3 MB, less than 6.88% of Python3 online submissions for ZigZag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        memo = {}
        r_flag = False
        a_i = 0
        for val in s:
            # 一列毎に分けて格納
            if a_i in memo:
                memo[a_i] = memo[a_i]+val
            else:
                memo[a_i] = val
            # 端までいくと折り返し
            if r_flag == False and a_i == numRows-1:
                r_flag = True
            elif r_flag == True and a_i == 0:
                r_flag = False
            #状態に応じて進む方向を変える
            if r_flag:
                a_i -= 1
            else:
                a_i += 1
        ans = ''
        for key, val in memo.items():
            ans = ans+val
        return ans