from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        max_dis = []

        points.sort(key=lambda x: x[0] + x[1])
        max_dis.append(self.fun(points[1:]))
        max_dis.append(self.fun(points[:-1]))

        points.sort(key=lambda x: x[0] - x[1])
        max_dis.append(self.fun(points[1:]))
        max_dis.append(self.fun(points[:-1]))

        return min(max_dis)

    def fun(self, points):
        mx_out = max(u + v for u, v in points)
        mn_out = min(u + v for u, v in points)

        mx_in = max(u - v for u, v in points)
        mn_in = min(u - v for u, v in points)

        return max(mx_out - mn_out, mx_in - mn_in)
