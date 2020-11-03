# https://leetcode.com/problems/multiply-strings/
# Runtime: 140 ms, faster than 38.97% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Multiply Strings.

class Solution:
    def multiply(self, a1: str, a2: str) -> str:    
        ans = [0] * (len(a1) + len(a2))
        k = -1
        for x in reversed(a1):
            for j,y in enumerate(reversed(a2)):
                z = int(x)*int(y)+ans[k-j]
                ans[k-j] = z%10
                ans[k-j-1] += z//10
            k -= 1
        h = 0
        while h < len(ans)-1 and ans[h] == 0: h += 1
        return ''.join(map(str, ans[h:]))