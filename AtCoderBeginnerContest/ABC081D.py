# https://atcoder.jp/contests/abc081/tasks/arc086_b

N = int(input())
A = list(map(int,input().split()))
plus_cnt, minus_cnt = 0, 0
for a in A:
    if 0 <= a:
        plus_cnt += 1
    if a <= 0:
        minus_cnt += 1
ans = []
if plus_cnt == N:
    for i in range(1,N):
        ans.append([i,i+1])
elif minus_cnt == N:
    for i in range(N-1, 0, -1):
        ans.append([i+1,i])
else:
    max_val = max(A)
    min_val = min(A)
    if abs(min_val) <= max_val:
        max_i = A.index(max_val)
        for i in range(N):
            if A[i] < 0:
                A[i] += max_val
                ans.append([max_i+1, i+1])
        for i in range(1,N):
            ans.append([i,i+1])
    else:
        min_i = A.index(min_val)
        for i in range(N):
            if 0 < A[i]:
                A[i] += min_val
                ans.append([min_i+1, i+1])
        for i in range(N-1, 0, -1):
            ans.append([i+1,i])

print(len(ans))
for a in ans:
    print(*a)