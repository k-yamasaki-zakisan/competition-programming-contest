# https://leetcode.com/problems/string-without-aaa-or-bbb/
# Runtime: 30 ms, faster than 96.68% of Python3 online submissions for String Without AAA or BBB.
# Memory Usage: 13.9 MB, less than 25.51% of Python3 online submissions for String Without AAA or BBB.


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def create_text(f: int, s: int, f_cnt: int, s_cnt: int) -> None:
            text = ""
            while f_cnt:
                text += f
                f_cnt -= 1
                if f_cnt and s_cnt <= f_cnt:
                    text += f
                    f_cnt -= 1
                if s_cnt:
                    text += s
                    s_cnt -= 1
            return text

        ans = ""
        if b < a:
            ans = create_text("a", "b", a, b)
        elif a < b:
            ans = create_text("b", "a", b, a)
        else:
            ans = "ab" * a

        return ans
