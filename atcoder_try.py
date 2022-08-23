# from collections import Counter
# import re
# import copy
# import itertools
# from sys import stdin
# from collections import deque
# from copy import copy
# from itertools import combinations
# from bisect import bisect
# import heapq
# import sys
# from collections import defaultdict
# memo = defaultdict(int)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float("inf")
MOD1 = 10**9 + 7
MOD2 = 998244353

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
S = set([0])
sum_a = 0
for a in A:
    sum_a += a
    S.add(sum_a)
for s in S:
    if s + P in S and s + P + Q in S and s + P + Q + R in S:
        print("Yes")
        exit()
print("No")


class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        result, opened = "", 0

        for char in s:
            if char == "(" and opened > 0:
                result += char
            if char == ")" and opened > 1:
                result += char

            if char == "(":
                opened += 1
            else:
                opened -= 1
        return result
