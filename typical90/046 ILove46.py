# https://atcoder.jp/contests/typical90/tasks/typical90_at

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
a_remainder = [0]*46
b_remainder = [0]*46
c_remainder = [0]*46
for i in range(N):
    a_remainder[A[i] % 46] += 1
    b_remainder[B[i] % 46] += 1
    c_remainder[C[i] % 46] += 1
ans = 0
for i_a in range(46):
    for i_b in range(46):
        for i_c in range(46):
            if (i_a + i_b + i_c) % 46 == 0:
                ans += a_remainder[i_a]*b_remainder[i_b]*c_remainder[i_c]
print(ans)
