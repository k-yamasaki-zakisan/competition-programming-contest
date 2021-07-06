# https://atcoder.jp/contests/typical90/tasks/typical90_cg

K = int(input())
ans = 0
for a in range(1, 10001):
    if K % a:
        continue
    max_bc = K//a
    for b in range(a, int(max_bc**0.5)+1):
        if K//(a*b) < b:
            break
        if K % (a*b) == 0 and b <= K//(a*b):
            ans += 1
print(ans)
