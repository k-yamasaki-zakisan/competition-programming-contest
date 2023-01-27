from math import ceil

from collections import defaultdict

len_nums = 3
dp = [[defaultdict(int) for _ in range(len_nums)] for _ in range(len_nums)]
print(dp[0])
dp[0][0][1] += 1
print(dp[0])
