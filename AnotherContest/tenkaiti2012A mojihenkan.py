#https://atcoder.jp/contests/tenka1-2012-qualA/tasks/tenka1_2012_qualA_2

t = list(input())
ans = []
flag = False
for i in range(len(t)):
    if flag:
        flag = False
        if t[i+1] ==' ':
            flag = True
    elif t[i] ==' ':
        ans.append(',')
        if t[i+1] ==' ':
            flag = True
    else:
        ans.append(t[i])
print(''.join(map(str,ans)))
