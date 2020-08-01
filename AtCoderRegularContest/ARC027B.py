#https://atcoder.jp/contests/arc027/tasks/arc027_2

num_check  = []
for i in range(10):
    num_check.append(str(i))

n=int(input())

s_1=list(input())

s_2=list(input())

alf = {}

for i in range(n):
    if s_1[i] in num_check and s_2[i] not in num_check:
        alf[s_2[i]] = 1
    elif s_2[i] in num_check and s_1[i] not in num_check:
        alf[s_1[i]] = 1

count = 1

for i in range(n):
    if s_1[i] not in num_check and s_2[i] not in num_check:
        if s_1[i] not in alf and s_2[i] not in alf:
            alf[s_1[i]] = 1
            alf[s_2[i]] = 1
            if i == 0:
                count *= 9
            else:
                count *= 10
        elif s_1[i] not in alf:
            alf[s_1[i]] = 1
        elif s_2[i] not in alf:
            alf[s_2[i]] = 1
print(count)
