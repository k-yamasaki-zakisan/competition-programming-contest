#https://atcoder.jp/contests/abc140/tasks/abc140_d

n,k = map(int,input().split())

s=list(input())

now_happy_count = 0

for i in range(n-1):
    if s[i] == s[i+1]:
        now_happy_count += 1

index = 0

reverse_candidate = []

while index < n:
    if s[index] != s[0]:
        start = index
        while index < n and s[index] != s[0]:
            index += 1
        end = index - 1
        reverse_candidate.append([start, end])
    else:
        index += 1

if len(reverse_candidate) <= k:
    print(n-1)
else:
    print(now_happy_count+2*k)
   
