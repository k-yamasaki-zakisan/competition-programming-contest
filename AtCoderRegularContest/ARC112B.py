# https://atcoder.jp/contests/arc112/tasks/arc112_b

B, C = map(int, input().split())
if B != 0:
    ans = 2
else:
    ans = 1

if B == 0:
    C_incost = C
    C_outcost = C
elif B < 0:
    B = -B
    C_incost = C-1
    C_outcost = C
else:
    C_incost = C
    C_outcost = C-1

# Bの内側の計算
if 0 < B-(C_incost//2):
    ans += C_incost//2*2-1
    if C_incost % 2:
        ans += 1
else:
    ans = B*2+1

# Bの外側の計算
ans += max(C_outcost//2*2-1, 0)
if C_outcost % 2 and C_outcost != 1:
    ans += 1
print(ans)
