# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Runtime: 20 ms, faster than 98.83% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.1 MB, less than 99.99% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> list:
        trans = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        ans = []
        if 0 < len(digits):
            for val1 in trans[digits[0]]:
                if 1 < len(digits):
                    for val2 in trans[digits[1]]:
                        if 2 < len(digits):
                            for val3 in trans[digits[2]]:
                                if 3 < len(digits):
                                    for val4 in trans[digits[3]]:
                                        ans.append(val1+val2+val3+val4)
                                else:
                                    ans.append(val1+val2+val3)
                        else:
                            ans.append(val1+val2)
                else:
                    ans.append(val1)
        return ans