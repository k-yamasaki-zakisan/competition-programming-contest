# https://leetcode.com/problems/minimum-area-rectangle/
# Runtime: 1236 ms, faster than 58.38% of Python3 online submissions for Minimum Area Rectangle.
# Memory Usage: 14.6 MB, less than 80.82% of Python3 online submissions for Minimum Area Rectangle.

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        from collections import defaultdict
        x_ys = defaultdict(set)
        for point in points:
            x, y = point
            x_ys[x].add(y)
        for key in list(x_ys.keys()):
            if len(x_ys[key]) < 2:
                del x_ys[key]
        ans = 10**10
        for key_1, set_vals_1 in x_ys.items():
            sort_vals_1 = sorted(set_vals_1)
            for key_2, set_vals_2 in x_ys.items():
                if key_1 == key_2:
                    continue
                for i in range(len(sort_vals_1)-1):
                    ii = sort_vals_1[i]
                    for j in range(i+1, len(sort_vals_1)):
                        jj = sort_vals_1[j]
                        if ii in set_vals_2 and jj in set_vals_2:
                            ans = min(ans, abs(key_2-key_1)*abs(jj-ii))
        if ans == 10**10:
            return 0
        return ans
