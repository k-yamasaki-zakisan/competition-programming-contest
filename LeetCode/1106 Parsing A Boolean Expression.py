# https://leetcode.com/problems/parsing-a-boolean-expression/
# Runtime: 1358 ms, faster than 5.28% of Python3 online submissions for Parsing A Boolean Expression.
# Memory Usage: 14.3 MB, less than 12.87% of Python3 online submissions for Parsing A Boolean Expression.


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
