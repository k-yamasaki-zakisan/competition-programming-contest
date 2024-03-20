class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        count = 1
        prevlast = points[0][1]

        for i in range(1, len(points)):
            if prevlast >= points[i][0]:
                pass
            else:
                prevlast = points[i][1]
                count += 1

        return count
