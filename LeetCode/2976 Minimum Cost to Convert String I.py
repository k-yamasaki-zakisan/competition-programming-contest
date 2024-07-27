from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        root = defaultdict(list)
        for i in range(len(original)):
            root[original[i]].append([changed[i], cost[i]])
        convert = defaultdict(int)
        letter_kings = list(set(list(source + target)))
        for letter in letter_kings:
            heapq_list = [[0, letter]]
            convert[(letter, letter)] = 0
            while len(heapq_list):
                now_cost, s = heappop(heapq_list)
                for change_s, change_cost in root[s]:
                    if (letter, change_s) in convert and convert[
                        (letter, change_s)
                    ] <= now_cost + change_cost:
                        continue
                    convert[(letter, change_s)] = now_cost + change_cost
                    heappush(heapq_list, [now_cost + change_cost, change_s])
        ans = 0
        for i in range(len(source)):
            if (source[i], target[i]) not in convert:
                return -1
            ans += convert[(source[i], target[i])]
        return ans
