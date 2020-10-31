# https://leetcode.com/problems/4sum/
#Runtime: 1024 ms, faster than 40.46% of Python3 online submissions for 4Sum.
#Memory Usage: 14.1 MB, less than 10.41% of Python3 online submissions for 4Sum.
# 集合のゴリ押しでパフォーマンス

class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        nums.sort()
        len_n = len(nums)
        ans = set()
        print(nums)
        for i in range(len_n-3):
            if 0 < i and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len_n-2):
                if 1 < j and nums[j] == nums[j-1] == nums[j-2]:
                    continue
                left = j+1
                right = len_n-1
                while left < right:
                    sums = nums[i]+nums[j]+nums[left]+nums[right]
                    if sums < target:
                        left += 1
                    elif target < sums:
                        right -= 1
                    else:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        while left < right and nums[left]==nums[left+1]:
                            left += 1
                        while left > right and nums[right]==nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return list(ans)