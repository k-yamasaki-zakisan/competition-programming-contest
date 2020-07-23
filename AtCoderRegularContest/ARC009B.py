#https://atcoder.jp/contests/arc009/tasks/arc009_2

b = list(map(int,input().split()))

n=int(input())
number = []
for _ in range(n):
    s=input()
    number.append(s)

big_small = {}

for i in range(len(b)):
    big_small[str(b[i])] = str(i)

trans_number = []

for i in range(n):
    num_break = list(number[i])
    keta = len(num_break)
    tmp_num = ""
    for j in num_break:
        tmp_num = tmp_num + big_small[j]
    trans_number.append([int(tmp_num),i])

trans_number = sorted(trans_number, key=lambda x:x[0])

#print(trans_number)

for key,val in trans_number:
    print(number[val])
