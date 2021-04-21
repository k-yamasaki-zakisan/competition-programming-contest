# https://leetcode.com/problems/image-overlap/
# Runtime: 2780 ms, faster than 5.04% of Python3 online submissions for Image Overlap.
# Memory Usage: 14.3 MB, less than 83.45% of Python3 online submissions for Image Overlap.

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        max_h = len(img1)
        max_w = len(img1[0])
        ans = 0
        for nh in range(-max_h, max_h):
            for nw in range(-max_w, max_w):
                tmp = 0
                for h in range(max_h):
                    for w in range(max_w):
                        if 0 <= nh+h < max_h and 0 <= nw+w < max_w:
                            if img1[h][w] == img2[h+nh][w+nw] == 1:
                                tmp += 1
                ans = max(ans, tmp)
        return ans
