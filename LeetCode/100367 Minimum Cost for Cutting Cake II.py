from typing import List


class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        cuts = [(cost, "h") for cost in horizontalCut] + [
            (cost, "v") for cost in verticalCut
        ]
        cuts.sort(reverse=True)

        horizontal_pieces = 1
        vertical_pieces = 1

        total_cost = 0

        for cost, cut_type in cuts:
            if cut_type == "h":
                total_cost += cost * vertical_pieces
                horizontal_pieces += 1
            else:
                total_cost += cost * horizontal_pieces
                vertical_pieces += 1

        return total_cost
