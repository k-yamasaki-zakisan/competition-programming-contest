from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        zahyo = []
        for start, end in flowers:
            zahyo.append(start)
            zahyo.append(end + 1)
        for p in people:
            zahyo.append(p)
        zahyo.sort()

        (*XS,) = set(zahyo)
        XS.sort()
        zahyo = {e: i for i, e in enumerate(XS)}

        N = len(XS)

        memo = [0] * N
        for start, end in flowers:
            memo[zahyo[start]] += 1
            memo[zahyo[end + 1]] -= 1
        for i in range(1, N):
            memo[i] += memo[i - 1]

        ans = []
        for p in people:
            ans.append(memo[zahyo[p]])
        return ans
