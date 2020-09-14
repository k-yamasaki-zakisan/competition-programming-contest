#https://atcoder.jp/contests/abc178/tasks/abc178_d

mod = 1000000007

N = int(input())
memo = [0]*(N+1)
for i in range(3,N+1):
    tmp = 1
    for j in range(i-3):
        tmp += memo[j+1]
    memo[i] = tmp%mod
print(memo[-1])
