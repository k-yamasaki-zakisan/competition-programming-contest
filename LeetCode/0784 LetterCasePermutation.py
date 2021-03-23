# https://leetcode.com/problems/letter-case-permutation/
# Runtime: 100 ms, faster than 15.10% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 14.8 MB, less than 60.61% of Python3 online submissions for Letter Case Permutation.


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        alph = [chr(ord('a') + i) for i in range(26)]
        s_downcase = S.lower()
        memo = []
        for i, s in enumerate(s_downcase):
            if s in alph:
                memo.append(i)

        ans = []
        for i in range(2 ** len(memo)):
            bag = []
            for j in range(len(memo)):
                if ((i >> j) & 1):
                    bag.append(memo[j])

            tmp = ''
            for i, s in enumerate(s_downcase):
                if i in bag:
                    tmp += s.upper()
                else:
                    tmp += s
            ans.append(tmp)
        return ans
