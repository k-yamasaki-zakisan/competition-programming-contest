#https://atcoder.jp/contests/abc136/tasks/abc136_d

s=list(input())

border = []

for i in range(len(s)-1):
    if s[i] == 'R' and s[i+1] == 'L':
        border.append(i)

border.append(-1)

left = right = border[0]

k = 0

ans = [0]*len(s)

for i in range(len(s)):
    if i == right:
        ans[i] += 1
        continue
    if i == right + 1:
        ans[i] += 1
        left = right
        right = border[k+1]
        k += 1
        continue
    if s[i] == "R":
        ans[right + (right-i)%2] += 1
    else:
        ans[left + (i-left)%2] += 1
print(*ans)
