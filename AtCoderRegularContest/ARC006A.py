e = list(map(int,input().split()))
B = int(input())
l = list(map(int,input().split()))

memo = [0,0,0,5,4,3,1]

e_memo = [0]*10

for i in e:
    e_memo[i] = 1

ans = 0
for i in l:
    if e_memo[i] == 1:
        ans += 1

if ans == 5:
    for i in l:
        if e_memo[i] != 1:
            if B == i:
                print(2)
            else:
                print(memo[ans])
elif 3 <= ans <= 6:
    print(memo[ans])
else:
    print(0)