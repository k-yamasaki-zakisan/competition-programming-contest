#https://atcoder.jp/contests/abc043/tasks/arc059_b

s=input()

s=list(s)

for i in range(1,len(s)):
    if i==1:
        if s[i] == s[i-1]:
            print(i,i+1)
            exit()
    elif s[i] == s[i-1]:
        print(i,i+1)
        exit()
    elif s[i] == s[i-2]:
        print(i-1,i+1)
        exit()
print(-1, -1)
