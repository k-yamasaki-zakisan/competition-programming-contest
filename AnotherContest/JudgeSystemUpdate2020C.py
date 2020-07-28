#https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c

import itertools

a = list(map(int,input().split()))

num_range = []
for i in range(1, sum(a)+1):
    num_range.append(i)

ans = 0

for v in itertools.permutations(num_range, sum(a)):
    dp = [[-1 for i in range(3)] for j in range(3)]
    index = 0
    for i in range(3):
        for j in range(3):
            if i < a[j]:
                dp[i][j] = v[index]
                index += 1
    flag = True
    for i in range(3):
        for j in range(3):
            if dp[i][j] == -1:
                continue
            
            if j == 0 and i == 0:
                continue
            elif i == 0:
                if dp[i][j] < dp[i][j-1]:
                    flag = False
            elif j == 0:
                if dp[i][j] < dp[i-1][j]:
                    flag = False
            else:
                if dp[i][j] < dp[i-1][j] or dp[i][j] < dp[i][j-1]:
                    flag = False

            if flag == False:
                break
        if flag == False:
                break
    if flag:
        ans += 1
print(ans)
