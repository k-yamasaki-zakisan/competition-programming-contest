# https://atcoder.jp/contests/arc126/tasks/arc126_a

T = int(input())
cases = [list(map(int, input().split())) for _ in range(T)]
for case in cases:
    N2, N3, N4 = case
    N6 = N3//2
    tmp = 0
    tmp1 = min(N6, N4)
    N6 -= tmp1
    N4 -= tmp1
    tmp2 = 0
    if N6 and 2 <= N2:
        tmp2 += min(N6, N2//2)
        N6 -= tmp2
        N2 -= tmp2*2
    tmp3 = 0
    if 2 <= N4 and N2:
        tmp3 += min(N4//2, N2)
        N4 -= tmp3*2
        N2 -= tmp3
    tmp4 = 0
    if N4 and 2 < N2:
        tmp4 += min(N4, N2//3)
        N4 -= tmp4
        N2 -= tmp4*3
    tmp5 = N2//5
    print(tmp1+tmp2+tmp3+tmp4+tmp5)
