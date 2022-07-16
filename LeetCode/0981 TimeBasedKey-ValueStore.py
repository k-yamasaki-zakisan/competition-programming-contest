# https://leetcode.com/problems/time-based-key-value-store/
# Runtime: 872 ms, faster than 76.08% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 70.9 MB, less than 87.79% of Python3 online submissions for Time Based Key-Value Store.

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.key_value_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value_store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_value_store:
            return ""
        if self.key_value_store[key][-1][-1] <= timestamp:
            return self.key_value_store[key][-1][0]
        if timestamp < self.key_value_store[key][0][-1]:
            return ""

        l, r = 0, len(self.key_value_store[key])
        while l < r:
            m = l + (r - l) // 2
            if self.key_value_store[key][m][-1] > timestamp:
                r = m
            else:
                l = m + 1

        return self.key_value_store[key][l - 1][0]
