#https://atcoder.jp/contests/abc163/tasks/abc163_d

mod = 1000000007

n,k = map(int,input().split())

memo = []

for i in range(n+1):
  memo.append(i)

min_sum = [0]

for i in range(1,n+1):
  kazu = memo[i]+min_sum[i-1]
  min_sum.append(kazu)

memo.reverse()

max_sum = [memo[0]]

for i in range(1,n+1):
  kazu = memo[i]+max_sum[i-1]
  max_sum.append(kazu)

ans = 0

for i in range(k-1,n+1):
  ans += max_sum[i]-min_sum[i]+1

print(ans%mod)
