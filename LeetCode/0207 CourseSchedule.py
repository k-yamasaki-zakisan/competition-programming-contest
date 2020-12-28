# https://leetcode.com/problems/course-schedule/
# Runtime: 1744 ms, faster than 5.03% of Python3 online submissions for Course Schedule.
# Memory Usage: 15.5 MB, less than 78.96% of Python3 online submissions for Course Schedule.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        seen = set()
        while prerequisites:
            a, b = prerequisites.pop()
            if [b, a] in prerequisites:
                return False
            for x, y in prerequisites:
                if x == b:
                    if [y, a] in prerequisites:
                        return False
                    else:
                        if (a, b) not in seen:
                            prerequisites.append([a, y])
                            seen.add((a, b))
        return True
