from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum([len(g) for g in garbage])
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        travel = [0] + travel
        g_posi = [i for i, g in enumerate(garbage) if "G" in g]
        m_posi = [i for i, g in enumerate(garbage) if "M" in g]
        p_posi = [i for i, g in enumerate(garbage) if "P" in g]
        print(g_posi, m_posi, p_posi)
        for i in range(len(g_posi)):
            i_i = g_posi[i]
            i_i_ex = g_posi[i - 1]
            if i == 0 and i_i != 0:
                ans += travel[i_i]
            elif i_i != 0:
                ans += travel[i_i] - travel[i_i_ex]
            print(ans, travel, i_i)
        for i in range(len(m_posi)):
            i_i = m_posi[i]
            i_i_ex = m_posi[i - 1]
            if i == 0 and i_i != 0:
                ans += travel[i_i]
            elif i_i != 0:
                ans += travel[i_i] - travel[i_i_ex]
        for i in range(len(p_posi)):
            i_i = p_posi[i]
            i_i_ex = p_posi[i - 1]
            if i == 0 and i_i != 0:
                ans += travel[i_i]
            elif i_i != 0:
                ans += travel[i_i] - travel[i_i_ex]
        return ans


S = Solution()
garbage = ["MMM", "PGM", "GP"]
travel = [3, 10]
print(S.garbageCollection(garbage, travel))
