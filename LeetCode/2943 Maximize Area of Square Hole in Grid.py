from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        hBars.sort()
        vBars.sort()
        h_max = 0
        h_cnt = 1
        for i in range(1, len(hBars)):
            if hBars[i] - hBars[i - 1] == 1:
                h_cnt += 1
            else:
                h_max = max(h_max, h_cnt)
                h_cnt = 1
        h_max = max(h_max, h_cnt)

        v_max = 0
        v_cnt = 1
        for i in range(1, len(vBars)):
            if vBars[i] - vBars[i - 1] == 1:
                v_cnt += 1
            else:
                v_max = max(v_max, v_cnt)
                v_cnt = 1
        v_max = max(v_max, v_cnt)
        return min(h_max + 1, v_max + 1) ** 2
