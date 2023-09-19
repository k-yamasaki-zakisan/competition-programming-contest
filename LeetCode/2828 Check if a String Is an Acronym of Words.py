from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        sum_head = ""
        for word in words:
            sum_head += word[0]
        return sum_head == s
