class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num_list = list(num)
        while len(num_list) and num_list[-1] == "0":
            num_list.pop()
        return "".join(num_list)
