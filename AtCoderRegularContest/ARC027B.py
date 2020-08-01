#https://atcoder.jp/contests/arc027/tasks/arc027_2

#case_1
n = int(input())
s1 = input()
s2 = input()

for i in range(n):
    c1 = s1[i]
    c2 = s2[i]
    if 'A' <= c1 <= 'Z':
        if 'A' <= c2 <= 'Z':
            if c1 != c2:
                s1 = s1.replace(c2, c1)
                s2 = s2.replace(c2, c1)
        else:
            s1 = s1.replace(c1, c2)
            s2 = s2.replace(c1, c2)
    else:
        if 'A' <= c2 <= 'Z':
            s1 = s1.replace(c2, c1)
            s2 = s2.replace(c2, c1)

ans = 1
d = set()
for i in range(n):
    if 'A' <= s1[i] <= 'Z' and s1[i] not in d:
        d.add(s1[i])
        if i == 0:
            ans *= 9
        else:
            ans *= 10

print(ans)


#case_2
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
