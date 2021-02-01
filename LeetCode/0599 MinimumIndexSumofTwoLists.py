# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Runtime: 160 ms, faster than 45.46% of Python3 online submissions for Minimum Index Sum of Two Lists.
# Memory Usage: 14.9 MB, less than 43.17% of Python3 online submissions for Minimum Index Sum of Two Lists.

class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        memo = {}
        for i, l1 in enumerate(list1):
            if l1 not in memo:
                memo[l1] = i
        tmp = []
        for i, l2 in enumerate(list2):
            if l2 in memo:
                tmp.append([i+memo[l2], l2])
        tmp.sort()
        ans = []
        for sum_i, restran in tmp:
            if tmp[0][0] == sum_i:
                ans.append(restran)
            else:
                break
        return ans
