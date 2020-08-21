#https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b

n = int(input())
A = []
B = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    A.append(a)
    B.append(b)

A.sort()
s = A[len(A)//2]
B.sort()
g = B[len(B)//2]

ans = 0

for i in range(n):
    ans += abs(A[i]-B[i])
    ans += abs(A[i]-s)
    ans += abs(B[i]-g)
print(ans)
