# https://leetcode.com/problems/sort-array-by-parity-ii/
# Runtime: 196 ms, faster than 97.90% of Python3 online submissions for Sort Array By Parity II.
# Memory Usage: 16.7 MB, less than 43.06% of Python3 online submissions for Sort Array By Parity II.

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        ans = []
        for i in range(len(odd)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
