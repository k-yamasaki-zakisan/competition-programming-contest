# https://atcoder.jp/contests/arc123/tasks/arc123_a

A1, A2, A3 = map(int, input().split())
tmp = A1+A3+1 if (A1+A3) % 2 else A1+A3
ans = 0
if A2*2 <= tmp:
    if (A1+A3) % 2:
        ans = (A1+A3+1)//2-A2+1
    else:
        ans = (A1+A3)//2-A2
else:
    if (A1+A3) % 2:
        center = (A1+A3+1)//2
        ans += 1
    else:
        center = (A1+A3)//2
    ans += abs(center-A2)*2

print(ans)
