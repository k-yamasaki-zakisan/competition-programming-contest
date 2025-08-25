class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        H, W = len(mat), len(mat[0])
        max_cnt = H * W
        is_right = True
        now_h, now_w = 0, 0
        ans = [mat[now_h][now_w]]
        while len(ans) < max_cnt:
            next_h, next_w = now_h, now_w
            next_is_right = is_right
            if is_right:
                if 0 <= now_h - 1 and now_w + 1 < W:
                    next_h -= 1
                    next_w += 1
                else:
                    next_is_right = False
            else:
                if now_h + 1 < H and 0 <= now_w - 1:
                    next_h += 1
                    next_w -= 1
                else:
                    next_is_right = True

            if next_is_right != is_right:
                if is_right:
                    if next_w == W - 1:
                        next_h += 1
                    else:
                        next_w += 1
                else:
                    if next_h == H - 1:
                        next_w += 1
                    else:
                        next_h += 1
            now_h = next_h
            now_w = next_w
            is_right = next_is_right
            ans.append(mat[now_h][now_w])
        return ans
