class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_tmp = []
        for ss in s:
            if ss == "#":
                if len(s_tmp):
                    s_tmp.pop()
            else:
                s_tmp.append(ss)
        t_tmp = []
        for tt in t:
            if tt == "#":
                if len(t_tmp):
                    t_tmp.pop()
            else:
                t_tmp.append(tt)
        return "".join(s_tmp) == "".join(t_tmp)
