from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        cells = []
        for ba in bank:
            cnt_one = len([b for b in ba if b == "1"])
            if 0 < cnt_one:
                cells.append(cnt_one)
        ans = 0
        for i in range(1, len(cells)):
            ans += cells[i] * cells[i - 1]
        return ans
