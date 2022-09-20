# https://leetcode.com/problems/occurrences-after-bigram/
# Runtime: 45 ms, faster than 61.64% of Python3 online submissions for Occurrences After Bigram.
# Memory Usage: 13.7 MB, less than 96.48% of Python3 online submissions for Occurrences After Bigram.


from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        return [
            words[i + 1]
            for i in range(1, len(words) - 1)
            if (words[i - 1] == first and words[i] == second)
        ]
