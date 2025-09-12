class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = ("a", "e", "i", "o", "u")
        cnt = 0
        for i in s:
            if i in vowels:
                cnt += 1
        if cnt == 0:
            return False
        return True
