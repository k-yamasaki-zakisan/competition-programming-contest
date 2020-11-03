# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Runtime: 80 ms, faster than 86.32% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if nums == []:
            return [-1,-1]
        ok = len(nums)-1
        ng = 0
        while 1<ok-ng:
            mid = (ok+ng)//2
            if target <= nums[mid]:
                ok = mid
            else:
                ng = mid
        i = ng if nums[ng] == target else ok
        if nums[i] == target:
            j = i
            while j+1 < len(nums):
                if nums[j+1] == target:
                    j += 1
                else:
                    break
            if i < j:
                return [i, j]
            else:
                return [i, i]
        else:
            return [-1,-1]


# Runtime: 84 ms, faster than 67.60% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

if nums == []:
            return [-1,-1]
        nums.append(10**10)
        ok = len(nums)-1
        ng = 0
        while 1<ok-ng:
            mid = (ok+ng)//2
            if target <= nums[mid]:
                ok = mid
            else:
                ng = mid
        i = ng if nums[ng] == target else ok
        ok = len(nums)-1
        ng = 0
        while 1<ok-ng:
            mid = (ok+ng)//2
            if target < nums[mid]:
                ok = mid
            else:
                ng = mid
        j = ng if nums[ng] == target else ok
        if nums[i] == target:
            if i < j:
                return [i, j]
            else:
                return [i, i]
        else:
            return [-1,-1]