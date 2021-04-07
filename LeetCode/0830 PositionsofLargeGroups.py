# https://leetcode.com/problems/positions-of-large-groups/
# Runtime: 40 ms, faster than 53.13% of Python3 online submissions for Positions of Large Groups.
# Memory Usage: 14.2 MB, less than 83.81% of Python3 online submissions for Positions of Large Groups.

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        len_s = len(s)
        ans = []
        start = 0
        while start < len_s:
            count = 0
            now = start+1
            while now < len_s:
                if s[start] != s[now]:
                    break
                now += 1
                count += 1
            if 2 <= count:
                ans.append([start, start+count])
                start += count
            else:
                start += 1
        return ans
