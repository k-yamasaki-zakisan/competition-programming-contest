from typing import List

INF = 10**16


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        min_costs = {}
        for i, word in enumerate(words):
            if word not in min_costs:
                min_costs[word] = costs[i]
            else:
                min_costs[word] = min(min_costs[word], costs[i])
        n = len(target)

        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            for word, cost in min_costs.items():
                if target.startswith(word, i):
                    dp[i + len(word)] = min(dp[i + len(word)], dp[i] + cost)

        return dp[-1] if dp[-1] != INF else -1
