from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        now = 0
        for arrival, time in customers:
            now = max(now, arrival) + time
            wait_time += now - arrival
        return wait_time / len(customers)
