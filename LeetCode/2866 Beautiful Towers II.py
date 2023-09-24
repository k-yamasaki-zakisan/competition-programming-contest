from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)

        left = [0] * n
        stack = [-1]
        cur = 0
        for i in range(n):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= (j - stack[-1]) * maxHeights[j]
            cur += (i - stack[-1]) * maxHeights[i]
            stack.append(i)
            left[i] = cur

        stack = [n]
        res = cur = 0
        for i in range(n - 1, -1, -1):
            while len(stack) > 1 and maxHeights[stack[-1]] > maxHeights[i]:
                j = stack.pop()
                cur -= abs(j - stack[-1]) * maxHeights[j]
            cur += -(i - stack[-1]) * maxHeights[i]
            stack.append(i)
            res = max(res, left[i] + cur - maxHeights[i])

        return res
