# https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Runtime: 76 ms, faster than 60.78% of Python3 online submissions for Peak Index in a Mountain Array.
# Memory Usage: 15.3 MB, less than 58.81% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        len_arr = len(arr)
        for i in range(len_arr-1):
            if arr[i] > arr[i+1]:
                return i
        return len_arr-1
