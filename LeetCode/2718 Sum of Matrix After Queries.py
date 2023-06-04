from typing import List


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        memo_row = set()
        memo_clu = set()
        queries.reverse()
        ans = 0
        for t, i, val in queries:
            if t == 0:
                if i in memo_row:
                    continue
                ans += val * (n - len(memo_clu))
            if t == 1:
                if i in memo_clu:
                    continue
                ans += val * (n - len(memo_row))

            if t == 0:
                memo_row.add(i)
            if t == 1:
                memo_clu.add(i)
        return ans
