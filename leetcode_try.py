from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def deleteString(self, S: str) -> int:
        ans = 0
        flag = True
        while flag:
            flag = False
            for j in range(len(S) // 2 + 1):
                for i in range(len(S) // 2):
                    if (
                        # i + j + 2 + j < len(S) and
                        S[i : i + j + 1]
                        == S[i + j + 1 : i + j + 2 + j]
                    ):
                        # print(S[i : i + j + 1], S[i + j + 1 : i + j + 2 + j])
                        ans += 1
                        print(S[:i], S[i + j + 1 :], i, j)
                        S = S[:i] + S[i + j + 1 :]
                        print(S)
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                break
        return ans + 1


S = Solution()
s = "aaabaab"
print(S.deleteString(s))
