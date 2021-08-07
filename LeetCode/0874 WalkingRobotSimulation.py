# https://leetcode.com/problems/walking-robot-simulation/
# Runtime: 364 ms, faster than 59.40% of Python3 online submissions for Walking Robot Simulation.
# Memory Usage: 20.1 MB, less than 71.04% of Python3 online submissions for Walking Robot Simulation.

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dire = 0
        def changeDire(command:int, dire):
            if command == -1:
                dire += 1
            else:
                dire -= 1

            if dire == 4:
                dire = 0
            elif dire == -1:
                dire = 3
            
            return dire

        pos_obstacles = set()
        for obstacle in obstacles:
            pos_obstacles.add(tuple(obstacle))

        now = [0,0]
        ans = 0
        for command in commands:
            if command < 0:
                dire = changeDire(command, dire)
            if 0 < command:
                for _ in range(command):
                    if dire == 0:
                        if (now[0], now[1]+1) in pos_obstacles:
                            break
                        now[1] += 1
                    elif dire == 1:
                        if (now[0]+1, now[1]) in pos_obstacles:
                            break
                        now[0] += 1
                    elif dire == 2:
                        if (now[0], now[1]-1) in pos_obstacles:
                            break
                        now[1] -= 1
                    else:
                        if (now[0]-1, now[1]) in pos_obstacles:
                            break
                        now[0] -= 1
                ans = max(ans, now[0]**2+now[1]**2)
        return ans
