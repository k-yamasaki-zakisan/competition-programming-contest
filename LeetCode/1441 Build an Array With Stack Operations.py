from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        point = 0
        tmp = []
        ans = []
        for num in range(1, n + 1):
            ans.append("Push")
            tmp.append(num)
            if tmp[-1] == target[point]:
                point += 1
            else:
                ans.append("Pop")

            if point == len(target):
                return ans
        return ans
