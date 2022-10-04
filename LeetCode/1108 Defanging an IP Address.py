# https://leetcode.com/problems/defanging-an-ip-address/
# Runtime: 62 ms, faster than 16.23% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.8 MB, less than 48.72% of Python3 online submissions for Defanging an IP Address.


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
