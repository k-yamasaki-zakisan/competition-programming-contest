from typing import List
from heapq import heappush, heappop


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ave_heap = []
        for now_pass, now_total in classes:
            ave = now_pass / now_total
            new_ave = (now_pass + 1) / (now_total + 1)
            heappush(ave_heap, [-(new_ave - ave), now_pass, now_total])
        print(ave_heap)
        for _ in range(extraStudents):
            _, now_pass, now_total = heappop(ave_heap)
            ave = (now_pass + 1) / (now_total + 1)
            new_ave = (now_pass + 2) / (now_total + 2)
            heappush(ave_heap, [-(new_ave - ave), now_pass + 1, now_total + 1])
        print(ave_heap)
        return sum([now_pass / now_total for _, now_pass, now_total in ave_heap]) / len(
            classes
        )
