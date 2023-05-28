from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        ans = []
        for h in range(H):
            tmp = []
            for w in range(W):
                up = set()
                now_h, now_w = h, w
                for _ in range(H):
                    now_h -= 1
                    now_w -= 1
                    if 0 <= now_h < H and 0 <= now_w < W:
                        up.add(grid[now_h][now_w])
                    else:
                        break
                down = set()
                now_h, now_w = h, w
                for _ in range(H):
                    now_h += 1
                    now_w += 1
                    if 0 <= now_h < H and 0 <= now_w < W:
                        down.add(grid[now_h][now_w])
                    else:
                        break
                tmp.append(abs(len(up) - len(down)))
            ans.append(tmp)
        return ans
