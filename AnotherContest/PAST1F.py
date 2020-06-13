#https://atcoder.jp/contests/past201912-open/tasks/past201912_f

s=list(input())

ans = []

check = [chr(ord('A') + i) for i in range(26)]

front = True

memo = []

for i in range(len(s)):
    if s[i] in check:
        if front:
            front = not front
            s[i] = s[i].lower()
            memo.append(s[i])
        else:
            front = True
            s[i] = s[i].lower()
            memo.append(s[i])
            ans.append(''.join(map(str,memo)))
            memo = []
    else:
        memo.append(s[i])

ans.sort()

ans2 = []

for i in ans:
    i = list(i)
    i[0] = i[0].upper()
    i[-1] = i[-1].upper()
    i = ''.join(map(str,i))
    ans2.append(i)
print(''.join(map(str,ans2)))
