from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        if b < a:
            a, b = b, a
        a_bin = bin(a)[2:].zfill(n)
        b_bin = bin(b)[2:].zfill(n)
        ex_b = ""
        if len(a_bin) != len(b_bin):
            diff = len(b_bin) - len(a_bin)
            ex_b = b_bin[:diff]
            b_bin = b_bin[diff:]
        x_bin = ""
        first = True if ex_b == "" else False
        for i in range(n):
            if a_bin[i] == b_bin[i]:
                if a_bin[i] == "0":
                    x_bin += "1"
                else:
                    x_bin += "0"
            else:
                if first:
                    first = False
                    x_bin += "1" if b_bin[i] == "0" else "0"
                else:
                    x_bin += "1" if a_bin[i] == "0" else "0"
        x = int(x_bin, 2)
        # print(x, x_bin, a_bin, b_bin)
        return ((a ^ x) % MOD * (b ^ x) % MOD) % MOD


S = Solution()
a = 0
b = 3
n = 1
print(S.maximumXorProduct(a, b, n))
# 10
