#https://atcoder.jp/contests/abc034/tasks/abc034_d

n, k = map(int, input().split())
 
w = [0 for _ in range(n)]
p = [0 for _ in range(n)]
for i in range(n):
    w[i], p[i] = map(int, input().split())

a, b = 0, 100
#平均値の最大化
while b-a > 0.00000000001:
    c = (a + b) / 2
    s = []
    for i in range(n):
        tmp_concentration = w[i]*p[i]-c*w[i]
        s.append(tmp_concentration)
    s.sort(reverse=True)
    concentration = sum(s[:k])
    if 0 <= concentration:
        a = c
    else:
        b = c

print(c)
