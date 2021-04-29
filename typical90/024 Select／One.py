# https://atcoder.jp/contests/typical90/tasks/typical90_x

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tmp = 0
for i in range(N):
    tmp += abs(A[i]-B[i])
if tmp <= K and tmp % 2 == K % 2:
    print('Yes')
else:
    print('No')
