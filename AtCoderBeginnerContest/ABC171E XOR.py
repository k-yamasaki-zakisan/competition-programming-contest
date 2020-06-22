#https://atcoder.jp/contests/abc171/tasks/abc171_e

n=int(input())

t = list(map(int,input().split()))

sum_xor = t[0]

for i in range(1,n):
    sum_xor = sum_xor ^ t[i]

ans = []

for i in t:
    ans.append(sum_xor ^ i)

print(*ans)
