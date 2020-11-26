# https://leetcode.com/problems/largest-number/
# Runtime: 56 ms, faster than 16.29% of Python3 online submissions for Largest Number.
# Memory Usage: 14.2 MB, less than 14.85% of Python3 online submissions for Largest Number.

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num