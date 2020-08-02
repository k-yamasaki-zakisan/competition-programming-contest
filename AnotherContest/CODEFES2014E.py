#https://atcoder.jp/contests/code-festival-2014-final/tasks/code_festival_final_e

n=int(input())

r = list(map(int,input().split()))

reduce_r = [r[0]]

for i in range(1,n):
    if r[i-1] != r[i]:
        reduce_r.append(r[i])

up_count = 0
down_count = 0
for i in range(1,len(reduce_r)):
    if reduce_r[i-1] < reduce_r[i]:
        up_count += 1
    if reduce_r[i-1] > reduce_r[i]:
        down_count += 1

count = 1

for i in range(1,len(reduce_r)-1):
    if i == len(reduce_r)-2:
        if reduce_r[i-1] < reduce_r[i] > reduce_r[i+1] or reduce_r[i-1] > reduce_r[i] < reduce_r[i+1]:
            count += 2
        else:
            count += 1
    else:
        if reduce_r[i-1] < reduce_r[i] > reduce_r[i+1] or reduce_r[i-1] > reduce_r[i] < reduce_r[i+1]:
            count += 1


if up_count == len(reduce_r)-1 or down_count == len(reduce_r)-1:
    print(0)
else:
    print(count)
