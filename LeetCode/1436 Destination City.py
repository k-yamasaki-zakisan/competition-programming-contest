from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        from collections import defaultdict

        cnts = defaultdict(int)
        for sc, gc in paths:
            cnts[sc] += 1
            cnts[gc] -= 1
        for sc, gc in paths:
            if cnts[gc] == -1:
                return gc
        raise ValueError("There is loop!")
