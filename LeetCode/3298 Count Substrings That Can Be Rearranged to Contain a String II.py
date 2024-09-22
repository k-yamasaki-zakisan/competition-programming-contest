from collections import defaultdict, Counter


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        def is_valid(uniq_chr, now_cnt_chr, target_cnt_chr):
            for u in uniq_chr:
                if now_cnt_chr[u] < target_cnt_chr[u]:
                    return False
            return True

        n = len(word1)
        target_cnt_chr = Counter(word2)
        uniq_chr = set(list(word2))
        ans = 0
        tail = 0
        now_cnt_chr = defaultdict(int)
        for head in range(n):
            now_cnt_chr[word1[head]] += 1
            while tail <= head and is_valid(uniq_chr, now_cnt_chr, target_cnt_chr):
                ans += n - head
                now_cnt_chr[word1[tail]] -= 1
                tail += 1
        return ans
