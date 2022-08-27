from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips, key=lambda x: x[0])
        now = next = 0
        cnt = 1
        for s, g in clips:
            if s <= now <= g:
                next = max(next, g)
                if s <= time <= g:
                    return cnt
            elif g < now:
                continue
            else:
                if now < next:
                    cnt += 1
                    now = next
                    if now < s:
                        return -1
                    else:
                        next = max(next, g)
                        if s <= time <= g:
                            return cnt
        return -1


clips = [
    [0, 1],
    [6, 8],
    [0, 2],
    [5, 6],
    [0, 4],
    [0, 3],
    [6, 7],
    [1, 3],
    [4, 7],
    [1, 4],
    [2, 5],
    [2, 6],
    [3, 4],
    [4, 5],
    [5, 7],
    [6, 9],
]
time = 9

S = Solution()
print(S.videoStitching(clips, time))
