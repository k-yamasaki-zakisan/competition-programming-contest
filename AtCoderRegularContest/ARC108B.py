# https://atcoder.jp/contests/arc108/tasks/arc108_b

N = int(input())
S = input()
ans = ''
for s in S:
    ans += s
    if 2 < len(ans) and ans[-3:] == 'fox':
        ans = ans[:-3]
print(len(ans))