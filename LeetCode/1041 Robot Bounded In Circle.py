# https://leetcode.com/problems/robot-bounded-in-circle/
# Runtime: 57 ms, faster than 24.51% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 13.9 MB, less than 21.77% of Python3 online submissions for Robot Bounded In Circle.


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        l_d = {"N": "W", "E": "N", "S": "E", "W": "S"}
        r_d = {"N": "E", "E": "S", "S": "W", "W": "N"}
        now_d = "N"
        now_y, now_x = 0, 0
        for _ in range(4):
            for ins in instructions:
                if ins == "G":
                    if now_d == "N":
                        now_y += 1
                    elif now_d == "E":
                        now_x += 1
                    elif now_d == "S":
                        now_y -= 1
                    else:
                        now_x -= 1
                else:
                    if ins == "L":
                        now_d = l_d[now_d]
                    else:
                        now_d = r_d[now_d]
            if now_y == 0 and now_x == 0:
                return True
        return False
