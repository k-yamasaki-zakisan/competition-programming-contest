# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/
# Runtime: 2988 ms, faster than 46.31% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
# Memory Usage: 14.5 MB, less than 77.56% of Python3 online submissions for Length of Longest Fibonacci Subsequence.

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        ans = 0
        len_arr = len(arr)
        nums = set()
        for num in arr:
            nums.add(num)
        for i in range(len_arr-2):
            for j in range(i+1, len_arr-1):
                tmp = [arr[i], arr[j]]
                while tmp[-2]+tmp[-1] in nums and tmp[-2]+tmp[-1] <= arr[-1]:
                    tmp.append(tmp[-2]+tmp[-1])
                if 3 <= len(tmp):
                    ans = max(ans, len(tmp))
        if ans:
            return ans
        else:
            return 0