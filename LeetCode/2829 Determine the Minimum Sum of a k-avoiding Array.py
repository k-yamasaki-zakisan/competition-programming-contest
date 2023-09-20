class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans = [0]
        while len(ans) <= n:
            for num in range(ans[-1] + 1, 1000):
                flag = True
                for a in ans[1:]:
                    if a + num == k:
                        flag = False
                        break
                if flag:
                    ans.append(num)
                    break
            # print(ans,num)
        return sum(ans)
