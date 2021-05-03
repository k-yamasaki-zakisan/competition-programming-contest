# https://atcoder.jp/contests/typical90/tasks/typical90_ad

N, K = map(int, input().split())

nums_list = [0]*(10**7+1)
for i in range(3, 10**7+1, 2):
    num = i
    while num <= 10**7:
        nums_list[num] += 1
        num += i
memo = [0]*(10**7+1)
i = 2
while i <= 10**7:
    memo[i] += 1
    i += 2
for i in range(3, 10**7+1, 2):
    if i % 2 and nums_list[i] == 1:
        num = i
        while num <= 10**7:
            memo[num] += 1
            num += i
ans = 0
for i in range(2, N+1):
    if K <= memo[i]:
        ans += 1
print(ans)
