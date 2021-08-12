# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# Runtime: 744 ms, faster than 97.34% of Python3 online submissions for Bitwise ORs of Subarrays.
# Memory Usage: 40.8 MB, less than 64.64% of Python3 online submissions for Bitwise ORs of Subarrays.

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        buf = set()

        for a in arr:
            buf = {j | a for j in buf}
            buf.add(a)
            ans.update(buf)

        return len(ans)
