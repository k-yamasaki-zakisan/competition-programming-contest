N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
AB = sorted(AB, key=lambda x: -x[1])
AB = sorted(AB, key=lambda x: x[0])
a = AB[0][0]
b = 10**10
for i in range(1, N):
    b = min(b, AB[i][1])
ans = max(a, b)
AB = sorted(AB, key=lambda x: -x[0])
AB = sorted(AB, key=lambda x: x[1])
b = AB[0][1]
a = 10**10
for i in range(1, N):
    a = min(a, AB[i][0])
tmp = max(a, b)
ans = min(ans, tmp)
for a, b in AB:
    ans = min(ans, a+b)
print(ans)
