#https://atcoder.jp/contests/abc171/tasks/abc171_d

n=int(input())

t = list(map(int,input().split()))

first_sum = sum(t)

memo = [0]*(10**5+1)

for i in range(n):
    memo[t[i]] += 1

q=int(input())

for _ in range(q):
    b,c = map(int,input().split())
    first_sum += (c-b)*memo[b]
    print(first_sum)
    memo[c] += memo[b]
    memo[b] = 0
