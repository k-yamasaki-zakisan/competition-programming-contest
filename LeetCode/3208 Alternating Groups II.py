from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        tmp = 1
        n = len(colors) + k - 1
        colors_depli = colors * 2
        for i in range(1, n):
            if colors_depli[i - 1] != colors_depli[i]:
                tmp += 1
            else:
                tmp = 1
            if k <= tmp:
                ans += 1
        return ans
