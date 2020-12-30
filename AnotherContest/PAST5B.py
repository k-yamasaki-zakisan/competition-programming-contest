# https://atcoder.jp/contests/past202012-open/tasks/past202012_b

N = int(input())
S = input()
ans = ''
for i in range(N):
    ans = ans.replace(S[i], '')
    ans += S[i]
print(ans)
