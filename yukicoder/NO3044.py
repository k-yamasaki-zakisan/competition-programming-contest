#https://yukicoder.me/problems/no/3044

n,m = map(int,input().split())

a = list(map(int,input().split()))

memo_sum = 0

count = 0

anss = []

for i in range(n):
    if a[i]%2 == 1:
        count += 1
        memo_sum += a[i]
    else:
        if m <= count:
            anss.append(memo_sum)
        count = 0
        memo_sum = 0
if m <= count:
    anss.append(memo_sum)

for ans in anss:
    print(ans)
