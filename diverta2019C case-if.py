#https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c


n=int(input())
moji = []
for _ in range(n):
    s=input()
    moji.append(s)

mid_ab = 0
la_fb = 0
last_a = 0
first_b = 0

for s in moji:
    mojiretu=len(s)
    if s[0] == 'B' and s[-1] == 'A':
        la_fb += 1
    elif s[0] == 'B':
        first_b += 1
    elif s[-1] == 'A':
        last_a += 1
    for j in range(mojiretu-1):
        if s[j] == 'A' and s[j+1] == 'B':
            mid_ab += 1

if la_fb == 0:
    ans = mid_ab+min(last_a,first_b)
elif last_a == first_b == 0 and la_fb> 0:
    ans = mid_ab+la_fb-1
else:
    if la_fb <= abs(last_a-first_b):
        ans = mid_ab+min(last_a,first_b)+la_fb
    else:
        ans = mid_ab+max(last_a,first_b)+(la_fb-abs(last_a-first_b))
print(ans)
