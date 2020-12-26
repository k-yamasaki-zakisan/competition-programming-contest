# https://leetcode.com/problems/valid-anagram/
# Runtime: 60 ms, faster than 18.63% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 58.44% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if s == t:
            return True
        str_memo = {}
        for ss in s:
            if ss in str_memo:
                str_memo[ss] += 1
            else:
                str_memo[ss] = 1
        for tt in t:
            if tt in str_memo and str_memo[tt]:
                str_memo[tt] -= 1
            else:
                return False
        if max(str_memo.values()) == 0:
            return True
        else:
            return False


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         d = collections.defaultdict(int)

#         if (set(t).union(set(s)) != set(t)) or (set(t).union(set(s)) != set(s)):
#           return False

#         for char in s:
#           d[char] += 1

#         for char in t:
#           d[char] -= 1

#         for char in t:
#           if d[char] != 0:
#             return False

#         return True
