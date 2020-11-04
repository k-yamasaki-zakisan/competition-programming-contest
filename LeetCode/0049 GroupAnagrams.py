# https://leetcode.com/problems/group-anagrams/
# Runtime: 92 ms, faster than 89.47% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.1 MB, less than 11.93% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: list) -> list:
        memo = {}
        for i,val in enumerate(strs):
            val = list(val)
            val.sort()
            val = ''.join(val)
            if val in memo:
                memo[val].append(strs[i])
            else:
                memo[val] = [strs[i]]
        return memo.values()



# Runtime: 96 ms, faster than 77.65% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 11.93% of Python3 online submissions for Group Anagrams.

# class Solution:
#     def groupAnagrams(self, strs: list) -> list:
#         memo = {}
#         for i,val in enumerate(strs):
#             val = list(val)
#             val.sort()
#             val = ''.join(val)
#             if val in memo:
#                 memo[val].append(i)
#             else:
#                 memo[val] = [i]
#         result = [[] for _ in range(len(memo))]
#         i = 0
#         for key,val in memo.items():
#             for s_i in val:
#                 result[i].append(strs[s_i])
#             i += 1
#         return result