#https://atcoder.jp/contests/abc055/tasks/arc069_b

n=int(input())

s=list(input())

memo_ss = ['S','S']
memo_sw = ['S','W']
memo_ws = ['W','S']
memo_ww = ['W','W']

def check(memo_ss):
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
    return memo_ss

memo_ss = check(memo_ss)
memo_sw = check(memo_sw)
memo_ws = check(memo_ws)
memo_ww = check(memo_ww)

for memo in [memo_ss,memo_sw,memo_ws,memo_ww]:
    if memo[0] == memo[-1]:
        if s[0] == 'o':
            if memo[0] == 'S' and memo[1] == memo[n-1]:
                print(''.join(map(str,memo[:n])))
                exit()
            elif memo[0] == 'W' and memo[1] != memo[n-1]:
                print(''.join(map(str,memo[:n])))
                exit()
        elif s[0] == 'x':
            if memo[0] == 'S' and memo[1] != memo[n-1]:
                print(''.join(map(str,memo[:n])))
                exit()
            elif memo[0] == 'W' and memo[1] == memo[n-1]:
                print(''.join(map(str,memo[:n])))
                exit()
print(-1)
