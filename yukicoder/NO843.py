#https://yukicoder.me/problems/no/843

n=int(input())

prime = [0]*(n+1)

prime[1] = 1

for i in range(2,n+1):
    flag = True
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            flag = False
            break
    if flag:
        prime[i] = 1

r = 1

ans = 0

while r**2 <= n:
    for i in range(2,(r**2)//2+1):
        if prime[i] == 1 and prime[r**2-i] == 1:
            if i == r**2-i:
                ans += 1
            else:
                ans += 2
        #print(ans,i,r**2)
    r += 1

print(ans)
