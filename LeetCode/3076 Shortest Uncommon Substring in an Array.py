from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        ans = []
        defult = "z" * 30
        for i in range(n):
            tmp_strings = []
            ans_str = defult
            for j in range(n):
                if i == j:
                    continue
                tmp_strings.append(arr[j])
            for k in range(len(arr[i])):
                tmp_cnd = ""
                for l in range(k, len(arr[i])):
                    tmp_cnd += arr[i][l]
                    if all([tmp_cnd not in tmp_string for tmp_string in tmp_strings]):
                        if len(tmp_cnd) < len(ans_str):
                            ans_str = tmp_cnd
                        elif len(tmp_cnd) == len(ans_str) and tmp_cnd < ans_str:
                            ans_str = tmp_cnd
            if ans_str == defult:
                ans_str = ""
            ans.append(ans_str)
        return ans
