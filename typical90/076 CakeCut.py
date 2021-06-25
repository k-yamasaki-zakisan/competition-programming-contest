# https://atcoder.jp/contests/typical90/tasks/typical90_bx

N = int(input())
A = list(map(int, input().split()))
sum_A = sum(A)
averate_A = sum_A//10
if sum_A % 10 != 0:
    print('No')
    exit()
sum_num = 0
tail = 0
AA = A+A
for i, a in enumerate(AA):
    sum_num += a
    while tail < i and averate_A < sum_num:
        sum_num -= AA[tail]
        tail += 1
    if sum_num == averate_A:
        print('Yes')
        exit()
print('No')
