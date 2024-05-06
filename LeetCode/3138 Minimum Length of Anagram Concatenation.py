from collections import defaultdict


class Solution:
    def minAnagramLength(self, s: str) -> int:
        cnt_chr = defaultdict(int)
        for chara in s:
            cnt_chr[chara] += 1
        ans = cnt_chr[s[0]]
        for cnt in cnt_chr.values():
            ans = math.gcd(ans, cnt)
        return len(s) // ans
