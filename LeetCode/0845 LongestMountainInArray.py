# https://leetcode.com/problems/longest-mountain-in-array/
# Runtime: 164 ms, faster than 81.58% of Python3 online submissions for Longest Mountain in Array.
# Memory Usage: 15.3 MB, less than 47.61% of Python3 online submissions for Longest Mountain in Array.


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 0
        for i in range(1, N-1):
            if not(arr[i-1] < arr[i] > arr[i+1]):
                continue
            left, right = 0, 0
            for j in range(i-1, -1, -1):
                if arr[j] < arr[j+1]:
                    left += 1
                else:
                    break
            for j in range(i+1, N):
                if arr[j] < arr[j-1]:
                    right += 1
                else:
                    break
            if left and right:
                ans = max(ans, left+right+1)
        return ans
