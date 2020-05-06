#https://atcoder.jp/contests/code-formula-2014-qualb/tasks/code_formula_2014_qualB_b

s=list(input())

gu = 0

ki = 0

if len(s)%2==0:
    for i in range(len(s)):
        if i%2==0:
            ki += int(s[i])
        else:
            gu += int(s[i])
else:
    for i in range(len(s)):
        if i%2==1:
            ki += int(s[i])
        else:
            gu += int(s[i])
print(ki,gu)
