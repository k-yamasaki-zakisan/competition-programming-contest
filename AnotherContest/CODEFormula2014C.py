#https://atcoder.jp/contests/code-formula-2014-final/tasks/code_formula_2014_final_c

s=list(input())

alf = [chr(ord('a') + i) for i in range(26)]

index = 0

ans = []

while index < len(s)-1:
    memo = []
    flag=True
    if s[index] == '@' and s[index+1] in alf:
        flag=False
        index += 1
        for i in range(index,len(s)):
            if s[i] == ' ' or s[i] == '@':
                index=i
                break
            memo.append(s[i])
        moji = ''.join(map(str,memo))
        ans.append(moji)

    if flag:
        index += 1

ans = list(set(ans))

ans.sort()

if len(ans) > 0:
    for i in ans:
        print(i)
        
