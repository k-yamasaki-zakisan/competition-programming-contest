# https://leetcode.com/problems/jump-game-ii/
# Runtime: 124 ms, faster than 32.78% of Python3 online submissions for Jump Game II.
# Memory Usage: 18 MB, less than 5.14% of Python3 online submissions for Jump Game II.

class Solution:
    def jump(self, nums: list) -> int:
        if len(nums) == 1:
            return 0
        #key=ステップ数 val=その時に到達する最大のマス数
        min_step = {0:0}
        now_step = 0
        for i in range(len(nums)):
            if min_step[now_step] < i:
                while min_step[now_step] < i:
                    now_step += 1
            tmp_jump = nums[i]
            if now_step+1 in min_step:
                min_step[now_step+1] = max(i+tmp_jump, min_step[now_step+1])
            else:
                min_step[now_step+1] = i+tmp_jump

            if len(nums)-1 <= min_step[now_step+1]:
                return now_step+1