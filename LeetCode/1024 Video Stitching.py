# https://leetcode.com/problems/video-stitching/
# Runtime: 43 ms, faster than 79.00% of Python3 online submissions for Video Stitching.
# Memory Usage: 13.8 MB, less than 78.29% of Python3 online submissions for Video Stitching.


from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips)
        now = next = 0
        cnt = 1
        for s, g in clips:
            if now < s:
                cnt += 1
                now = next

            if s <= now <= g:
                next = max(next, g)
                if s <= time <= g:
                    return cnt
            elif now < s:
                return -1
        return -1
