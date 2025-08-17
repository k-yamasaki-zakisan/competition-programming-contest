class Solution:
    def maximum69Number(self, num: int) -> int:
        is_once_change = False
        ans = ""
        for n in str(num):
            if not is_once_change and n == "6":
                ans += "9"
                is_once_change = True
            else:
                ans += n
        return int(ans)
