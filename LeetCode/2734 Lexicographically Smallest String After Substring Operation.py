class Solution:
    def smallestString(self, s: str) -> str:
        i = 0
        N = len(s)
        ans = ""
        while i < N and s[i] == "a":
            ans += "a"
            i += 1
        if i == N:
            return s[:-1] + "z"

        change_flag = True
        for s_i in range(i, N):
            if s[s_i] == "a":
                change_flag = False

            if change_flag:
                ans += chr(ord(s[s_i]) - 1)
                continue
            ans += s[s_i]
        return ans
