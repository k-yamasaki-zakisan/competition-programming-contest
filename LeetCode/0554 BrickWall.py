# https://leetcode.com/problems/brick-wall/
# Runtime: 248 ms, faster than 10.89% of Python3 online submissions for Brick Wall.
# Memory Usage: 19.2 MB, less than 24.86% of Python3 online submissions for Brick Wall.

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        W = sum(wall[0])
        ans = len(wall)
        memo = defaultdict(int)
        for i in range(len(wall)):
            tmp = 0
            for w in wall[i]:
                tmp += w
                if tmp == W:
                    break
                memo[tmp] += 1
        if len(memo) == 0:
            return ans
        return ans-max(memo.values())
