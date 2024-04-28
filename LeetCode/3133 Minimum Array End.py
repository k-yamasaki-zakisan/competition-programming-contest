class Solution:
    def minEnd(self, n: int, x: int) -> int:
        base_bin = list(bin(x)[2:])
        target_bin = list(bin(n - 1)[2:])
        t_i = len(target_bin) - 1
        for i in range(len(base_bin) - 1, -1, -1):
            if base_bin[i] == "0" and 0 <= t_i:
                base_bin[i] = target_bin[t_i]
                t_i -= 1
        if 0 <= t_i:
            return int("".join(target_bin[: t_i + 1] + base_bin), 2)
        else:
            return int("".join(base_bin), 2)
