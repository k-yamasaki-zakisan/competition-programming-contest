# https://leetcode.com/problems/valid-mountain-array/
# Runtime: 204 ms, faster than 55.13% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.4 MB, less than 85.99% of Python3 online submissions for Valid Mountain Array.


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_p = arr.index(max(arr))
        len_arr = len(arr)
        if max_p == 0 or max_p == len_arr-1:
            return False
        for i in range(1, max_p+1):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(len_arr-2, max_p-1, -1):
            if arr[i] <= arr[i+1]:
                return False
        return True
