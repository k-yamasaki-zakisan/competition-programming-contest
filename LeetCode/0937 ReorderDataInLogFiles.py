# https://leetcode.com/problems/reorder-data-in-log-files/
# Runtime: 48 ms, faster than 12.61% of Python3 online submissions for Reorder Data in Log Files.
# Memory Usage: 14.4 MB, less than 37.30% of Python3 online submissions for Reorder Data in Log Files.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = filter(lambda l: l[l.find(" ") + 1].isalpha(), logs)
        d = filter(lambda l: l[l.find(" ") + 1].isdigit(), logs)
        return sorted(l, key=lambda x: (x[x.find(" "):], x[:x.find(" ")])) + list(d)
