# https://atcoder.jp/contests/abc227/tasks/abc227_d

N, K = map(int, input().split())
A = list(map(int, input().split()))
l, r = 0, 10**19
while 1 < r-l:
    mid = (r+l)//2
    sum_a = 0
    for a in A:
        sum_a += min(a, mid)
    if K*mid <= sum_a:
        l = mid
    else:
        r = mid
print(l)
