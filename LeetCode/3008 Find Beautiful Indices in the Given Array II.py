from typing import List


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        from bisect import bisect_left

        a_indices = self.kmp_search(s, a)
        b_indices = self.kmp_search(s, b)

        ans = []
        for a_i in a_indices:
            b_i = bisect_left(b_indices, a_i)
            if b_i < len(b_indices) and abs(b_indices[b_i] - a_i) <= k:
                ans.append(a_i)
            elif 0 <= b_i - 1 and abs(b_indices[b_i - 1] - a_i) <= k:
                ans.append(a_i)
        return ans

    def kmp_search(self, text, pattern):
        lps = self.compute_lps(pattern)
        occurrences = []

        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == len(pattern):
                occurrences.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return occurrences

    def compute_lps(self, pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
