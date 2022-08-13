# https://leetcode.com/problems/complement-of-base-10-integer/
# Runtime: 30 ms, faster than 94.21% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 13.9 MB, less than 55.97% of Python3 online submissions for Complement of Base 10 Integer.


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        reverse_bin = "".join(["0" if b == "1" else "1" for b in bin(n)[2:]])
        return int(reverse_bin, 2)
