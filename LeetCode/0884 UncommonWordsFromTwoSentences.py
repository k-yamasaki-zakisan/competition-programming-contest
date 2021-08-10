# https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Runtime: 28 ms, faster than 83.31% of Python3 online submissions for Uncommon Words from Two Sentences.
# Memory Usage: 14.1 MB, less than 94.54% of Python3 online submissions for Uncommon Words from Two Sentences.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Count All the Words
        counts = Counter(s1.split() + s2.split())

        # Find the Uncommon Words
        return [word for word, count in counts.items() if count == 1]

    # def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    #     from collections import Counter
    #     from collections import defaultdict
    #     s1_list = s1.split()
    #     s2_list = s2.split()
    #     ans = []
    #     s1_count = Counter(s1_list)
    #     s2_count = Counter(s2_list)
    #     for key, count in s1_count.items():
    #         if 2 <= count:
    #             continue
    #         if key not in s2_count:
    #             ans.append(key)
    #     for key, count in s2_count.items():
    #         if 2 <= count:
    #             continue
    #         if key not in s1_count:
    #             ans.append(key)
    #     return ans
