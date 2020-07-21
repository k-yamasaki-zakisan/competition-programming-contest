#https://atcoder.jp/contests/arc051/tasks/arc051_b

n=int(input())

memo = [0]*(n+2)
memo[0] = 1
memo[1] = 1

for i in range(2,n+2):
    memo[i] = memo[i-1]+memo[i-2]
#print(memo)

print(memo[n+1],memo[n])
