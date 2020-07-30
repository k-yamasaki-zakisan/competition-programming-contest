#https://yukicoder.me/problems/no/633

n=int(input())
ab = []
for _ in range(n-1):
    a = int(input())
    ab.append(a)
men_in_bus = 0
ans = 0
for i in range(n):
    b,c = map(int,input().split())
    if i == 0:
        men_in_bus += c
    elif i == n-1:
        break
    else:
        men_in_bus += c-b
    ans += men_in_bus*ab[i]
print(ans)
