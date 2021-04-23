# https://atcoder.jp/contests/typical90/tasks/typical90_a

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
A = [0] + A + [L]
ok = L
ng = 0
ans = 0
while ng+1 != ok:
    count = 0
    mid = (ok+ng)//2
    tmp_point = 0
    min_youkan = L
    for i in range(1, len(A)):
        if mid < A[i]-tmp_point:
            count += 1
            min_youkan = min(min_youkan, A[i]-tmp_point)
            tmp_point = A[i]
    if K < count:
        ng = mid
    else:
        ok = mid

print(ok)
