#https://atcoder.jp/contests/abc096/tasks/abc096_d

n=int(input())

prime = []

for i in range(11,55556,2):
    flag = True
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            flag=False
            break
    if flag:
        prime.append(i)
        
prime_mod1 = []

for i in prime:
    if i%5==1:
       prime_mod1.append(i)
print(*prime_mod1[:n])
