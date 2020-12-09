# https://atcoder.jp/contests/abc030/tasks/abc030_d

N,a = map(int,input().split())
a -= 1
K = int(input())
B = list(map(int,input().split()))
B = [b-1 for b in B]
jump = 0
i = a
root = [True]*N
while root[i] and jump < K:
    root[i] = False
    jump += 1
    i = B[i]

if jump == K:
    print(i+1)
else:
    K -= jump
    jump = 0
    jump_memo = [i]
    root = [True]*N
    while root[i] and jump < K:
        root[i] = False
        jump += 1
        i = B[i]
        jump_memo.append(i)
    if jump == K:
        print(i+1)
    else:
        i = K%jump
        print(jump_memo[i]+1)