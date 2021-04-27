# https://atcoder.jp/contests/typical90/tasks/typical90_n

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
ans = 0
for i in range(N):
    ans += abs(A[i]-B[i])
print(ans)
