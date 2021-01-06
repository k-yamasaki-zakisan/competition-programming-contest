# https://leetcode.com/problems/restore-ip-addresses/
# Runtime: 36 ms, faster than 58.05% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 14.4 MB, less than 27.71% of Python3 online submissions for Restore IP Addresses.

class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        n = len(list(s))
        ans = []
        for d1 in range(1, 4):
            for d2 in range(1, 4):
                for d3 in range(1, 4):
                    for d4 in range(1, 4):
                        if n == d1+d2+d3+d4:
                            block1 = s[0:d1]
                            block2 = s[d1:d1+d2]
                            block3 = s[d1+d2:d1+d2+d3]
                            block4 = s[d1+d2+d3:d1+d2+d3+d4]
                            if self.is_block(block1) \
                                    and self.is_block(block2) \
                                    and self.is_block(block3) \
                                    and self.is_block(block4):
                                ans.append(
                                    f"{block1}.{block2}.{block3}.{block4}")
        return ans

    def is_block(self, block: str) -> bool:
        if 1 < len(block) and block[0] == '0':
            return False
        return 0 <= int(block) <= 255
