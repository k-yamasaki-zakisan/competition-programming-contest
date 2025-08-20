class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        H, W = len(matrix), len(matrix[0])
        S = [[0] * (W + 1) for _ in range(H + 1)]
        for h in range(H):
            for w in range(W):
                S[h + 1][w + 1] = S[h + 1][w] + S[h][w + 1] - S[h][w] + matrix[h][w]
        ans = 0
        for h in range(H):
            for w in range(W):
                if matrix[h][w] == 0:
                    continue
                n_h, n_w = h + 1, w + 1
                while n_h <= H and n_w <= W:
                    now_ones = S[n_h][n_w] - S[n_h][w] - S[h][n_w] + S[h][w]
                    if now_ones == (n_h - h) ** 2:
                        ans += 1
                    n_h += 1
                    n_w += 1
        return ans
