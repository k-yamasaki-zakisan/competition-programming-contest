import sys

sys.set_int_max_str_digits(1000000)


class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1:
            return "9" * n
        elif k == 2:
            if 3 <= n:
                return "8" + "9" * (n - 2) + "8"
            else:
                return "8" * n
        elif k == 3:
            return "9" * n
        elif k == 4:
            if n <= 3:
                return "8" * n
            else:
                return "88" + "9" * (n - 4) + "88"
        elif k == 5:
            if n <= 2:
                return "5" * n
            return "5" + "9" * (n - 2) + "5"
        elif k == 6:
            if n <= 2:
                return "6" * n
            elif n == 3:
                return "888"
            elif n == 4:
                return "8778"
            elif n % 2 == 1:
                cent = 9 - ((16 + (n - 3) * 9) % 3)
                return (
                    "8" + "9" * ((n - 3) // 2) + str(cent) + "9" * ((n - 3) // 2) + "8"
                )
            else:
                return "8" + "9" * ((n - 4) // 2) + "77" + "9" * ((n - 4) // 2) + "8"
        elif k == 7:
            if n <= 2:
                return "7" * n
            if n % 2 == 1:
                for i in range(10, -1, -1):
                    tmp = "9" * (n // 2) + str(i) + "9" * (n // 2)
                    if int(tmp) % 7 == 0:
                        return tmp
            else:
                for i in range(10, -1, -1):
                    tmp = "9" * ((n - 2) // 2) + str(i) * 2 + "9" * ((n - 2) // 2)
                    if int(tmp) % 7 == 0:
                        return tmp
        elif k == 8:
            if n <= 6:
                return "8" * n
            return "888" + "9" * (n - 6) + "888"
        elif k == 9:
            return "9" * n
