#https://atcoder.jp/contests/abc059/tasks/arc072_a

n=int(input())

a = list(map(int,input().split()))

memo_1 = [0]*n
memo_1_ruiseki = [0]*n
memo_2 = [0]*n
memo_2_ruiseki = [0]*n

for i in range(n):
    if i%2==0:
        if memo_1_ruiseki[i-1]+a[i] < 0:
            memo_1[i] = abs(memo_1_ruiseki[i-1])+1
        elif memo_1_ruiseki[i-1]+a[i] == 0:
            memo_1[i] = a[i]+1
        else:
            memo_1[i] = a[i]
    else:
        if memo_1_ruiseki[i-1]+a[i] > 0:
            memo_1[i] = -1+(-1)*abs(memo_1_ruiseki[i-1])
        elif memo_1_ruiseki[i-1]+a[i] == 0:
            memo_1[i] = -1+a[i]
        else:
            memo_1[i] = a[i]
    memo_1_ruiseki[i] = memo_1_ruiseki[i-1]+memo_1[i]

for i in range(n):
    if i%2==1:
        if memo_2_ruiseki[i-1]+a[i] < 0:
            memo_2[i] = abs(memo_2_ruiseki[i-1])+1
        elif memo_2_ruiseki[i-1]+a[i] == 0:
            memo_2[i] = a[i]+1
        else:
            memo_2[i] = a[i]
    else:
        if memo_2_ruiseki[i-1]+a[i] > 0:
            memo_2[i] = -1+(-1)*abs(memo_2_ruiseki[i-1])
        elif memo_2_ruiseki[i-1]+a[i] == 0:
            memo_2[i] = -1+a[i]
        else:
            memo_2[i] = a[i]
    memo_2_ruiseki[i] = memo_2_ruiseki[i-1]+memo_2[i]

ans_1 = 0
ans_2 = 0

for i in range(n):
    ans_1 += abs(memo_1[i]-a[i])
    ans_2 += abs(memo_2[i]-a[i])

print(min(ans_1,ans_2))
