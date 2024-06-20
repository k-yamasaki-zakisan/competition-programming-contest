from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l, r = 0, position[-1]
        while 1 < r - l:
            mid = (l + r) // 2
            cnt = 1
            ex_ball_position = position[0]
            for i in range(1, len(position)):
                if mid <= position[i] - ex_ball_position:
                    cnt += 1
                    ex_ball_position = position[i]
            if cnt < m:
                r = mid
            else:
                l = mid
        return l
