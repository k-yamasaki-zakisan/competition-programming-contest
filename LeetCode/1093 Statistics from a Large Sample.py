# https://leetcode.com/problems/statistics-from-a-large-sample/
# Runtime: 88 ms, faster than 43.62% of Python3 online submissions for Statistics from a Large Sample.
# Memory Usage: 14 MB, less than 48.40% of Python3 online submissions for Statistics from a Large Sample.

from typing import List


class Solution:
    def sampleStats(self, counts: List[int]) -> List[float]:
        arg_sum = cnt = 0
        min_num = float("inf")
        max_num = -1
        max_count = 0
        max_count_val = 0
        for i, count in enumerate(counts):
            if count:
                min_num = min(min_num, i)
                max_num = max(max_num, i)
                arg_sum += i * count
                cnt += count
            if max_count < count:
                max_count = count
                max_count_val = i
        if cnt % 2 == 0:
            tag1, tag2 = cnt // 2, (cnt + 2) // 2
            re_cnt = 0
            for i, count in enumerate(counts):
                if re_cnt < tag1 <= re_cnt + count:
                    tag1_val = i
                if re_cnt < tag2 <= re_cnt + count:
                    tag2_val = i
                    break
                re_cnt += count
            mid = (tag1_val + tag2_val) / 2
        else:
            tag = (cnt + 1) // 2
            re_cnt = 0
            for i, count in enumerate(counts):
                if re_cnt < tag <= re_cnt + count:
                    mid = i
                    break
                re_cnt += count
        return [min_num, max_num, arg_sum / cnt, mid, max_count_val]
