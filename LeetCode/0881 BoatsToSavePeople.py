# https://leetcode.com/problems/boats-to-save-people/
# Runtime: 1136 ms, faster than 5.02% of Python3 online submissions for Boats to Save People.
# Memory Usage: 19.4 MB, less than 97.78% of Python3 online submissions for Boats to Save People.

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        from bisect import bisect_right
        people.sort()
        ans = 0
        while len(people):
            base = people.pop()
            tmp = limit-base
            if len(people) and people[0] <= tmp:
                i = bisect_right(people, tmp)-1
                people.pop(i)
            ans += 1
        return ans
