#https://atcoder.jp/contests/past201912-open/tasks/past201912_d

n=int(input())
ab = [0]*n
for _ in range(n):
    a=int(input())
    ab[a-1] += 1

for i in range(n):
    if ab[i] == 0:
        change = i+1
    elif ab[i] == 2:
        changed = i+1

try:
    print(changed,change)
except:
    print('Correct')
