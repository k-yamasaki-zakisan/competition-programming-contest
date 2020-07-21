#https://atcoder.jp/contests/arc034/tasks/arc034_2

n=int(input())

ans = []

for i in range(max(1,n-200), n+1):
    tmp_f = 0
    list_i = list(str(i))
    for ii in list_i:
        tmp_f += int(ii)
    if n == tmp_f+i:
        ans.append(i)

print(len(ans))

for aa in ans:
    print(aa)
