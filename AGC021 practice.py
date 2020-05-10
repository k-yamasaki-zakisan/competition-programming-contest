#https://atcoder.jp/contests/agc021/tasks/agc021_a

s=list(input())

memo = []

for i in s:
    memo.append(int(i))

ans = max(sum(memo),(memo[0]-1)+(len(memo)-1)*9)

print(ans)
