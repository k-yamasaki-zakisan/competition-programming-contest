#https://atcoder.jp/contests/abc170/tasks/abc170_d

n = int(input())
a = sorted(list(map(int, input().split())))
if n == 1:
    print(1)
    exit()  
check_list = [0] * (10**6 + 2)
ans = 0
for i in range(n):
    tmp = a[i]
    while tmp <= a[-1]:
        check_list[tmp] += 1
        tmp += a[i]
for aa in a:
    if check_list[aa] == 1:
        ans += 1
print(ans)
