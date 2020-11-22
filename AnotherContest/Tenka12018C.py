# https://atcoder.jp/contests/tenka1-2018-beginner/tasks/tenka1_2018_c

N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
ans = 0
if N%2 == 0:
    ans = sum(A[N//2:])*2-sum(A[:N//2])*2+A[N//2-1]-A[N//2]
else:
    ans = max(sum(A[N//2+1:])*2-sum(A[:N//2+1])*2+A[N//2-1]+A[N//2],
            sum(A[N//2:])*2-sum(A[:N//2])*2-A[N//2+1]-A[N//2])
print(ans)