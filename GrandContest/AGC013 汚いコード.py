#https://atcoder.jp/contests/agc013/tasks/agc013_a

n=int(input())

a = list(map(int,input().split()))

index = 1

ans = 0

while index < n:
    ans += 1
    if a[index-1] < a[index]:
        flag = True
    elif a[index-1] > a[index]:
        flag = False
    else:
        flag3 = True
        for i in range(index,n):
            if a[index] != a[i]:
                flag3 = False
                if a[index] < a[i]:
                    flag = True
                    break
                else:
                    flag = False
                    break
        if flag3:
            break
    flag2 = True
    for i in range(index,n):
        if flag and a[i] < a[i-1]:
            index = i+1
            flag2 = False
            break
        elif a[i] > a[i-1] and flag == False:
            index = i+1
            flag2 = False
            break
    if flag2:
        break
if index == n:
    ans += 1
print(ans)
