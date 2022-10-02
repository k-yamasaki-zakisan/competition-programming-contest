# https://leetcode.com/problems/filling-bookcase-shelves/
# Runtime: 112 ms, faster than 28.47% of Python3 online submissions for Filling Bookcase Shelves.
# Memory Usage: 14.3 MB, less than 72.82% of Python3 online submissions for Filling Bookcase Shelves.

from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        len_books = len(books)
        dp = [float("inf") for _ in range(len_books + 1)]
        dp[0] = 0
        for i in range(1, len_books + 1):
            max_w = shelfWidth
            max_h = 0
            j = i - 1
            while 0 <= j and 0 <= max_w - books[j][0]:
                max_w -= books[j][0]
                max_h = max(max_h, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_h)
                j -= 1
        return dp[-1]
