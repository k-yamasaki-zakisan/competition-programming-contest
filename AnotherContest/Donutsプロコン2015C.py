#https://atcoder.jp/contests/donuts-2015/tasks/donuts_2015_3

N = int(input())

H = list(map(int,input().split()))

ans = [-1]*N

stack = []

for i,val in enumerate(H):
    ans[i] = len(stack)
    while 0 < len(stack):
        if stack[-1] < val:
            stack.pop()
        else:
            break
    stack.append(val)

for aa in ans:
    print(aa)
