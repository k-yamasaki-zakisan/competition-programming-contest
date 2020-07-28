#https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c

import itertools
import copy

a = list(map(int,input().split()))

dp = [[-1 for i in range(3)] for j in range(3)] 

num_range = []
for i in range(1, sum(a)+1):
    num_range.append(i)

ans = 0

for v in itertools.permutations(num_range, sum(a)):
    copy_dp = copy.deepcopy(dp)
    for i in range(3):
        for j in range(3):
            if i*3+j < len(v):
                copy_dp[i][j] = v[i*3+j]
    flag = True
    for i in range(3):
        for j in range(3):
            if copy_dp[i][j] == -1:
                break
            
            if j == 0 and i == 0:
                continue
            elif 0 < j and i == 0:
                if copy_dp[i][j] < copy_dp[i][j-1]:
                    flag = False
            elif j == 0 and 0 < i:
                if copy_dp[i][j] < copy_dp[i-1][j]:
                    flag = False
            else:
                if copy_dp[i][j] < copy_dp[i-1][j] or copy_dp[i][j] < copy_dp[i][j-1]:
                    flag = False

            if flag == False:
                break
        if flag == False:
                break
    if flag:
        ans += 1
print(ans)
