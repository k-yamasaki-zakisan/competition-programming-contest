#https://atcoder.jp/contests/arc019/tasks/arc019_2

n=list(input())

keta = len(n)

memo = [0]*keta

count = 0

for i in range(keta//2):
    #print(n[i], n[keta-1-i])
    if n[i] == n[keta-1-i]:
        memo[i] = 1
        memo[keta-1-i] = 1
        count += 1

if count == keta//2:
    ans = 2*count*25
elif count == keta//2-1:
    ans = (keta-2)*25+2*24
else:
    ans = keta*25

print(ans)
