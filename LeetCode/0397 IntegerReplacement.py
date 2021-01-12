# https://leetcode.com/problems/integer-replacement/
# Runtime: 80 ms, faster than 29.77% of Python3 online submissions for Integer Replacement.
# Memory Usage: 14.3 MB, less than 28.82% of Python3 online submissions for Integer Replacement.

class Solution:
    def integerReplacement(self, n: int) -> int:
        queue = collections.deque([n])
        step = -1
        visited = set()
        while len(queue):
            step += 1
            for _ in range(len(queue)):
                p = queue.popleft()
                if p == 1:
                    return step

                if p % 2:
                    queue.append(p+1)
                    queue.append(p-1)
                else:
                    queue.append(p//2)
