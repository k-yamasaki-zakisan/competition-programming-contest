from typing import List, Optional
from functools import lru_cache

# from collections import Counter

# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque

# MOD = 10**9 + 7


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        N = len(positions)
        cand = []
        for i in range(N):
            cand.append([positions[i], healths[i], directions[i], i])
            cand.sort()
        ans = [cand[0]]
        for i in range(1, N):
            if len(ans) == 0:
                ans.append(cand)
            elif ans[-1][2] == "R" and cand[i][2] == "L":
                if ans[-1][1] == cand[i][1]:
                    ans.pop
                elif ans[-1][1] > cand[i][1]:
                    ans[-1][1] -= 1
                else:
                    while len(ans):
                        if ans[-1][2] == "R" and cand[i][2] == "L":
                            if ans[-1][1] == cand[i][1]:
                                ans.pop
                                break
                            elif ans[-1][1] > cand[i][1]:
                                ans[-1][1] -= 1
                                break
                            else:
                                ans.pop()
                                cand[i][1] -= 1
                        else:
                            ans.append(cand[i])
            else:
                ans.append(cand[i])
        return ans


S = Solution()

positions = [5, 4, 3, 2, 1]
healths = [2, 17, 9, 15, 10]
directions = "RRRRR"
# 4
print(S.survivedRobotsHealths(positions, healths, directions))
