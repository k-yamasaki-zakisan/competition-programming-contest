#https://atcoder.jp/contests/abc055/tasks/arc069_b

n=int(input())

s=list(input())

memo_ss=['S','S']
memo_sw=['S','W']
memo_ws=['W','S']
memo_ww=['W','W']

for i in range(1,n):
    if s[i] == 'o' :
        if memo_ss[i] == 'S':
            if memo_ss[i-1] == 'S':
                memo_ss.append('S')
            elif memo_ss[i-1] == 'W':
                memo_ss.append('W')
        elif memo_ss[i] == 'W':
            if memo_ss[i-1] == 'S':
                memo_ss.append('W')
            elif memo_ss[i-1] == 'W':
                memo_ss.append('S')
    elif s[i] == 'x' :
        if memo_ss[i] == 'S':
            if memo_ss[i-1] == 'S':
                memo_ss.append('W')
            elif memo_ss[i-1] == 'W':
                memo_ss.append('S')
        elif memo_ss[i] == 'W':
            if memo_ss[i-1] == 'S':
                memo_ss.append('S')
            elif memo_ss[i-1] == 'W':
                memo_ss.append('W')
print(memo_ss)
