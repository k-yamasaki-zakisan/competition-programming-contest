# https://leetcode.com/problems/largest-time-for-given-digits/
# Runtime: 46 ms, faster than 55.76% of Python3 online submissions for Largest Time for Given Digits.
# Memory Usage: 13.9 MB, less than 77.78% of Python3 online submissions for Largest Time for Given Digits.

from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from collections import Counter

        ans = ""
        for h1 in range(3):
            if h1 not in arr:
                continue
            for h2 in range(10):
                if h2 not in arr:
                    continue
                if h1 == 2 and h2 not in (0, 1, 2, 3):
                    continue
                for h3 in range(6):
                    if h3 not in arr:
                        continue
                    for h4 in range(10):
                        if h4 not in arr:
                            continue
                        arr_cnt = Counter(arr)
                        ok_flag = True
                        for h in [h1, h2, h3, h4]:
                            if 0 < arr_cnt[h]:
                                arr_cnt[h] -= 1
                            else:
                                ok_flag = False
                                break
                        if ok_flag:
                            ans = f"{h1}{h2}:{h3}{h4}"
        return ans
