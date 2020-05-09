#https://atcoder.jp/contests/agc006/tasks/agc006_a

n=int(input())

s1=list(input())

s2=list(input())

ans = n*2

flag = False

for i in range(n):
    for j in range(n):
        if s1[i:n]==s2[j:n-i]:
            ans -= len(s1[i:n])
            flag = True
            break
    if flag:
        break

print(ans)
