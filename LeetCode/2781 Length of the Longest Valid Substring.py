from typing import List


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ans, cnt = 0, 0
        tmp = ""
        forbidden_set = set(forbidden)
        for i in range(len(word)):
            tmp += word[i]
            cnt += 1
            ng_flag = False
            tmp_cand = ""
            tmp_n = len(tmp)
            for j in range(min(tmp_n, 10)):
                tmp_cand = tmp[tmp_n - j - 1] + tmp_cand
                if tmp_cand in forbidden_set:
                    ng_flag = True
                    break
            if ng_flag:
                tmp = tmp_cand[1:]
                cnt = len(tmp)
            ans = max(ans, cnt)
        return ans
