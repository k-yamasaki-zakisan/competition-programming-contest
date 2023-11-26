from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        H = len(mat)
        W = len(mat[0])
        for h in range(H):
            for w in range(W):
                if h % 2 == 0:
                    if mat[h][(w + k) % W] != mat[h][w]:
                        return False
                else:
                    if mat[h][(W + w - k) % W] != mat[h][w]:
                        return False
        return True
