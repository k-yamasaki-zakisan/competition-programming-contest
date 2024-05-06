from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt_memo = defaultdict(int)
        i, n = 0, len(word)
        while i < n:
            cnt_memo[word[i : i + k]] += 1
            i += k
        max_cnt = max([cnt for cnt in cnt_memo.values()])
        return n // k - max_cnt
