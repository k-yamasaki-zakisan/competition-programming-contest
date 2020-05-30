#https://atcoder.jp/contests/agc003/tasks/agc003_b

n=int(input())
ab = []
for _ in range(n):
    a=int(input())
    ab.append(a)

ans = 0

for i in range(n):
    ans += ab[i]//2
    if i == n-1:
        break
    elif ab[i]%2 == 1 and ab[i+1] > 0:
        ans += 1
        ab[i+1] -= 1
print(ans)
