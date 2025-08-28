class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        H, W = len(grid), len(grid[0])
        for ori_h in range(H - 1, -1, -1):
            ori_w = 0
            now_h, now_w = ori_h, ori_w
            memo = []
            while now_h < H and now_w < W:
                memo.append(grid[now_h][now_w])
                now_h += 1
                now_w += 1
            now_h, now_w = ori_h, ori_w
            memo.sort(reverse=True)
            i = 0
            while now_h < H and now_w < W:
                grid[now_h][now_w] = memo[i]
                now_h += 1
                now_w += 1
                i += 1
        for ori_w in range(1, W):
            ori_h = 0
            now_h, now_w = ori_h, ori_w
            memo = []
            while now_h < H and now_w < W:
                memo.append(grid[now_h][now_w])
                now_h += 1
                now_w += 1
            now_h, now_w = ori_h, ori_w
            memo.sort()
            i = 0
            while now_h < H and now_w < W:
                grid[now_h][now_w] = memo[i]
                now_h += 1
                now_w += 1
                i += 1
        return grid
