# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
# Runtime: 28 ms, faster than 97.32% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.
# Memory Usage: 13.9 MB, less than 27.52% of Python3 online submissions for Path In Zigzag Labelled Binary Tree.

from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans, memo = [], [1]
        # layer内のrangeを事前に算出
        while memo[-1] < label:
            memo.append(memo[-1] * 2)
        now = label
        # 反転前のルートを算出
        while now != 1:
            ans = [now] + ans
            now //= 2
        ans = [1] + ans
        # 反転時のルートに調整
        for i in range(len(ans) - 2, -1, -2):
            first, last = memo[i], memo[i + 1] - 1
            ans[i] = last - (ans[i] - first)
        return ans
