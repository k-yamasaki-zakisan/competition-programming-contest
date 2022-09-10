# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Runtime: 214 ms, faster than 16.80% of Python3 online submissions for Remove All Adjacent Duplicates In String.
# Memory Usage: 14.7 MB, less than 97.59% of Python3 online submissions for Remove All Adjacent Duplicates In String.


class Solution:
    def removeDuplicates(self, s: str) -> str:
        from collections import deque

        ans = deque()
        for ss in s:
            if ans and ans[-1] == ss:
                ans.pop()
            else:
                ans.append(ss)
        return "".join(ans)
