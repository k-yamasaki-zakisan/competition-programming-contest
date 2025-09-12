class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u")
        cnt = 0
        for i in s:
            if i in vowels:
                return True
        return False
