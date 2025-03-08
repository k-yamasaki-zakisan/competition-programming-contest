class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = tmp = blocks[:k].count("W")
        for i in range(k, len(blocks)):
            if blocks[i - k] == "W":
                tmp -= 1
            if blocks[i] == "W":
                tmp += 1
            ans = min(ans, tmp)
        return ans
