from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        min_i, max_i = 0, n - 1
        same_boats_cnt = 0
        while min_i < max_i:
            if people[min_i] + people[max_i] <= limit:
                same_boats_cnt += 1
                min_i += 1
            max_i -= 1
        return n - same_boats_cnt
