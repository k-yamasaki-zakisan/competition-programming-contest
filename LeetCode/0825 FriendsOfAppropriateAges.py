# https://leetcode.com/problems/friends-of-appropriate-ages/
# Runtime: 420 ms, faster than 12.66% of Python3 online submissions for Friends Of Appropriate Ages.
# Memory Usage: 14.9 MB, less than 35.93% of Python3 online submissions for Friends Of Appropriate Ages.

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0]*121
        for age in ages:
            count[age] += 1

        ans = 0
        for age_a in range(len(count)):
            cnt_a = count[age_a]
            for age_b in range(len(count)):
                cnt_b = count[age_b]
                if age_b <= age_a*0.5+7:
                    continue
                if age_b > age_a:
                    continue
                if (age_b > 100 and age_a < 100):
                    continue

                ans += cnt_a*cnt_b
                if age_a == age_b:
                    ans -= cnt_a
        return ans
