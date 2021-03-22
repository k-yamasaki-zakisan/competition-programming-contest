# https://leetcode.com/problems/asteroid-collision/
# Runtime: 104 ms, faster than 44.01% of Python3 online submissions for Asteroid Collision.
# Memory Usage: 15.4 MB, less than 55.59% of Python3 online submissions for Asteroid Collision.


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [asteroids[0]]
        for i in range(1, len(asteroids)):
            if 0 < len(ans) and 0 < ans[-1] and asteroids[i] < 0:
                if ans[-1] + asteroids[i] == 0:
                    ans.pop()
                else:
                    if abs(ans[-1]) < abs(asteroids[i]):
                        ans[-1] = asteroids[i]
                        while 1 < len(ans) and 0 < ans[-2] and ans[-1] < 0:
                            tmp = ans.pop()
                            if abs(ans[-1]) == abs(tmp):
                                ans.pop()
                            elif abs(ans[-1]) < abs(tmp):
                                ans[-1] = tmp
            else:
                ans.append(asteroids[i])

        return ans
