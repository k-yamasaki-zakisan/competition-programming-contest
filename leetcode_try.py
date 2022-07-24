from typing import List

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        times = []
        for fs, fg in firstList:
            times.append([fs, 0, "f"])
            times.append([fg, 1, "f"])
        for ss, sg in secondList:
            times.append([ss, 0, "s"])
            times.append([sg, 1, "s"])
        times = sorted(times, key=lambda x: x[1])
        times = sorted(times, key=lambda x: x[0])

        ans = []
        len_times = len(times)
        for i in range(len_times - 1):
            f = times[i]
            s = times[i + 1]
            if f[0] == s[0] and f[1] == s[1]:
                if f[1] == 0:
                    times[i][2] = "fs"
                    times[i + 1][2] = "fs"
                else:
                    times[i][2] = "sf"
                    times[i + 1][2] = "sf"
        for i in range(len_times - 1):
            f = times[i]
            s = times[i + 1]
            if f[1] == 0 and s[1] == 1 and f[2] != s[2]:
                ans.append([f[0], s[0]])
        return ans


firstList = [[3, 5], [9, 20]]
secondList = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
# [[4,5],[9,10],[11,12],[14,15],[16,20]]
S = Solution()
print(S.intervalIntersection(firstList, secondList))
