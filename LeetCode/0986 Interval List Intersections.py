# https://leetcode.com/problems/interval-list-intersections/
# Runtime: 200 ms, faster than 65.46% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.8 MB, less than 86.30% of Python3 online submissions for Interval List Intersections.

from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        i, j = 0, 0
        len_f, len_s = len(firstList), len(secondList)
        res = []
        while i < len_f and j < len_s:
            s = max(firstList[i][0], secondList[j][0])
            e = min(firstList[i][1], secondList[j][1])
            if s <= e:
                res.append([s, e])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res


# しょぼ回答
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         ans = []
#         for fs, fg in firstList:
#             for ss,sg in secondList:
#                 if fs <= ss <= fg:
#                     ans.append([ss, min(fg, sg)])
#                 elif ss <= fs <= sg:
#                     ans.append([fs, min(fg, sg)])
#                 if fg < ss:
#                     break
#         return ans
