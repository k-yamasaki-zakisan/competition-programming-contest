# https://atcoder.jp/contests/past202010-open/tasks/past202010_i

N = int(input())
A = list(map(int,input().split()))
sum_a = sum(A)
A += A
tmp = 0
tail = 0
ans = 10**15
for i in range(2*N):
    tmp += A[i]
    while sum_a-tmp < tmp:
        tmp -= A[tail]
        tail += 1
    ans = min(ans, abs(sum_a-tmp*2))
print(ans)