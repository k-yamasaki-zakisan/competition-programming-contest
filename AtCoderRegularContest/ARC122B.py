# https://atcoder.jp/contests/arc122/tasks/arc122_b

def CheckCost(x):
    tmp_cost = 0
    for a in A:
        tmp_cost += a+x-min(a, 2*x)
    return tmp_cost/N


N = int(input())
A = list(map(int, input().split()))
low = 0
high = max(A)
cnt = 0
while cnt < 100:
    c1 = (low * 2 + high) / 3
    c2 = (low + high * 2) / 3
    if CheckCost(c1) > CheckCost(c2):
        low = c1
    else:
        high = c2
    cnt += 1
print(CheckCost(high))
