from typing import List, Optional
from collections import defaultdict, deque

# from collections import Counter
# from collections import defaultdict
# from bisect import bisect_right
# from copy import copy
# from collections import deque


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = list(expression)
        i = 0
        f = []
        while 1 < len(expression) and i < len(expression):
            if expression[i] == "(":
                f.append(i)
            elif expression[i] == ")":
                f_i = f.pop()
                tmp = []
                for t in range(f_i, i + 1):
                    if expression[t] == "t":
                        tmp.append(True)
                    elif expression[t] == "f":
                        tmp.append(False)
                if expression[f_i - 1] == "&":
                    expression = (
                        expression[: f_i - 1]
                        + ["t" if all(tmp) else "f"]
                        + expression[i + 1 :]
                    )
                elif expression[f_i - 1] == "|":
                    expression = (
                        expression[: f_i - 1]
                        + ["t" if any(tmp) else "f"]
                        + expression[i + 1 :]
                    )
                else:
                    expression = (
                        expression[: f_i - 1]
                        + ["t" if not tmp[0] else "f"]
                        + expression[i + 1 :]
                    )
                i = f_i - 2
            i += 1
        return True if expression[0] == "t" else False


S = Solution()
expression = "!(&(f,t))"
print(S.parseBoolExpr(expression))
