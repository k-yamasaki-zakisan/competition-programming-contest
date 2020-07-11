#https://yukicoder.me/problems/no/346

s=list(input())

ruiseki_w = [0]*len(s)

for i in range(len(s)):
    if s[i] == 'w':
        ruiseki_w[i] = 1+ruiseki_w[i-1]
    else:
        ruiseki_w[i] = ruiseki_w[i-1]

ans = 0

for i in range(len(s)):
    if s[i] == 'c':
        sum_c = ruiseki_w[-1]-ruiseki_w[i]
        ans += sum_c*(sum_c-1)//2
print(ans)
