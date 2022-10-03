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
        while 1 < len(expression):
            f = -1
            tmp = []
            for i in range(len(expression)):
                if expression[i] == "(":
                    f = i
                    tmp = []
                elif expression[i] == ")":
                    if expression[f - 1] == "&":
                        expression = (
                            expression[: f - 1]
                            + ["t" if all(tmp) else "f"]
                            + expression[i + 1 :]
                        )
                    elif expression[f - 1] == "|":
                        expression = (
                            expression[: f - 1]
                            + ["t" if any(tmp) else "f"]
                            + expression[i + 1 :]
                        )
                    else:
                        expression = (
                            expression[: f - 1]
                            + ["t" if not tmp[0] else "f"]
                            + expression[i + 1 :]
                        )
                    break
                else:
                    if expression[i] == "t":
                        tmp.append(True)
                    elif expression[i] == "f":
                        tmp.append(False)
        return True if expression[0] == "t" else False


S = Solution()
expression = "!(&(f,t))"
print(S.parseBoolExpr(expression))
