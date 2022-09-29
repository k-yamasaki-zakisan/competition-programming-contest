# https://leetcode.com/problems/find-in-mountain-array/
# Runtime: 43 ms, faster than 72.20% of Python3 online submissions for Find in Mountain Array.
# Memory Usage: 14.6 MB, less than 95.34% of Python3 online submissions for Find in Mountain Array.


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:
    def findInMountainArray(self, target: int, MA: "MountainArray") -> int:
        len_n = MA.length()
        l, r = 0, len_n - 1
        while l < r:
            mid = (l + r) // 2
            if MA.get(mid) < MA.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peak_i = l

        l, r = 0, peak_i
        while l <= r:
            mid = (l + r) // 2
            t = MA.get(mid)
            if t < target:
                l = mid + 1
            else:
                r = mid - 1
            if t == target:
                return mid

        l, r = peak_i + 1, len_n - 1
        while l <= r:
            mid = (l + r) // 2
            t = MA.get(mid)
            if target < t:
                l = mid + 1
            else:
                r = mid - 1
            if t == target:
                return mid
        return -1
