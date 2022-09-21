# https://leetcode.com/problems/letter-tile-possibilities/
# Runtime: 139 ms, faster than 59.87% of Python3 online submissions for Letter Tile Possibilities.
# Memory Usage: 15.7 MB, less than 50.11% of Python3 online submissions for Letter Tile Possibilities.


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations

        tiles_list = list(tiles)
        ans = set()
        for i in range(1, len(tiles_list) + 1):
            for v in permutations(tiles_list, i):
                ans.add(v)
        return len(ans)
