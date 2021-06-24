# https://atcoder.jp/contests/typical90/tasks/typical90_bw

N = int(input())
cnt = 0
for i in range(2, int(N**0.5)+1):
    while N % i == 0:
        cnt += 1
        N //= i

if N != 1:
    cnt += 1

ans = 0
tmp = 1
while tmp < cnt:
    ans += 1
    tmp *= 2
print(ans)
