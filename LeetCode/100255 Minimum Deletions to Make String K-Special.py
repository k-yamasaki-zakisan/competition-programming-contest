class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from bisect import bisect_left, bisect_right
        from collections import Counter

        cnt_memo = Counter(word)
        sort_cnt = [cnt for cnt in cnt_memo.values()]
        sort_cnt.sort()
        n = len(sort_cnt)
        ruiseki_cnt = [sort_cnt[0]]
        for i in range(1, n):
            ruiseki_cnt.append(ruiseki_cnt[-1] + sort_cnt[i])
        ans = float("inf")
        for cnt in sort_cnt:
            i_s = bisect_left(sort_cnt, cnt)
            i_l = bisect_right(sort_cnt, cnt + k) - 1
            tmp = 0
            if 0 < i_s:
                tmp += ruiseki_cnt[i_s - 1]
            if i_l + 1 < n:
                tmp += (ruiseki_cnt[-1] - ruiseki_cnt[i_l]) - (cnt + k) * (
                    n - (i_l + 1)
                )
            ans = min(ans, tmp)
        return ans
