# https://leetcode.com/problems/parsing-a-boolean-expression/
# Runtime: 454 ms, faster than 5.28% of Python3 online submissions for Parsing A Boolean Expression.
# Memory Usage: 14.3 MB, less than 19.80% of Python3 online submissions for Parsing A Boolean Expression.


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
