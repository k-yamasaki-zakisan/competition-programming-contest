from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        cnt = 0
        ans = ""
        for i in range(len(s)):
            ss = s[i : i + cnt + 1]
            moji = s[i + 1 :]
            while ss in moji:
                cnt += 1
                ans = ss
                ss = s[i : i + cnt + 1]
        return ans


S = Solution()
s = "abcd"
print(S.longestDupSubstring(s))
