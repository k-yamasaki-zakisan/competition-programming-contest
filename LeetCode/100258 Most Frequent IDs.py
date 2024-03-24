from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        from heapq import heappop, heappush
        from collections import defaultdict

        n = len(freq)
        memo = defaultdict(int)
        memo[0] = 1
        heapq_f = []
        ans = []
        for i in range(n):
            num = nums[i]
            memo[num] = max(memo[num] + freq[i], 0)
            heappush(heapq_f, [-memo[num], num])

            while len(heapq_f) and memo[heapq_f[0][1]] != -heapq_f[0][0]:
                heappop(heapq_f)
            # print(heapq_f, memo)
            if len(heapq_f):
                ans.append(abs(-heapq_f[0][0]))
            else:
                ans.append(0)
        return ans
