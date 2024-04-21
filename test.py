from collections import defaultdict

root_memo = defaultdict(lambda: defaultdict(int))
root_memo[1][2] = 1
print(root_memo[1][2])
