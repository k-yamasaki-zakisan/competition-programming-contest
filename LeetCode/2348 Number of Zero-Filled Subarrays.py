class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        tmp = 0
        for num in nums:
            if num == 0:
                tmp += 1
            else:
                tmp = 0
            ans += tmp
        return ans
