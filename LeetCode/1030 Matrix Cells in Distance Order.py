# https://leetcode.com/problems/matrix-cells-in-distance-order/
# Runtime: 366 ms, faster than 14.45% of Python3 online submissions for Matrix Cells in Distance Order.
# Memory Usage: 15.8 MB, less than 90.22% of Python3 online submissions for Matrix Cells in Distance Order.

from typing import List


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        return sorted(
            [[h, w] for h in range(rows) for w in range(cols)],
            key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter),
        )

        # ちょい改善解答
        # ans = []
        # for h in range(rows):
        #     for w in range(cols):
        #         ans.append([h,w,abs(h-rCenter)+abs(w-cCenter)])
        # return [[a,b] for a,b,c in sorted(ans, key=lambda x: x[2])]

        # 素朴な解答
        # from collections import deque
        # ans, visited = [[rCenter, cCenter]], set([(rCenter, cCenter)])
        # que = deque([[rCenter, cCenter]])
        # while len(que):
        #     h,w = que.popleft()
        #     for n_h, n_w in [(h+1, w),(h-1, w),(h, w+1),(h, w-1)]:
        #         if 0 <= n_h < rows and 0 <= n_w < cols and (n_h, n_w) not in visited:
        #             visited.add((n_h, n_w))
        #             ans.append([n_h, n_w])
        #             que.append([n_h, n_w])
        # return ans
