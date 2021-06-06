# https://atcoder.jp/contests/abc204/tasks/abc204_d

N = int(input())
T = list(map(int, input().split()))
total_num = sum(T)
memo = []
memo_list = [0]*(total_num+1)
for t in T:
    tmp = [t]
    memo_list[t] = 1
    for m in memo:
        next_num = m+t
        if memo_list[next_num] == 0:
            tmp.append(next_num)
            memo_list[next_num] = 1
    memo += tmp
ans = 10**10
for i, check in enumerate(memo_list):
    if check:
        ans = min(ans, max(i, total_num-i))
print(ans)
