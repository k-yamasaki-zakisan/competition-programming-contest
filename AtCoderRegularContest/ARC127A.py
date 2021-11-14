# https://atcoder.jp/contests/arc127/tasks/arc127_a

N = int(input())
len_n = len(str(N))

ans = 0
for i in range(1, len_n+1):
    tmp = '1'*i
    for j in range(len_n+1-i):
        st = int(tmp+'0'*j)
        if N < st:
            break
        en = int(tmp+'9'*j)
        ans += min(N-st+1, en-st+1)
print(ans)
