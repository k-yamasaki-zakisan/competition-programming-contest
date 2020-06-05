#https://atcoder.jp/contests/past202004-open/tasks/past202004_d

S = input()
ans = set()
for k in range(1, min(3, len(S))+1):
    ans.add("."*k)
    for i in range(len(S)-k+1):
        if k == 1:
            ans.add(S[i])
        elif k == 2:
            a, b = S[i], S[i+1]
            ans.add(a+b)
            ans.add(a+".")
            ans.add("."+b)
        else:
            a, b, c = S[i], S[i+1], S[i+2]
            ans.add(a+b+c)
            ans.add(a+b+".")
            ans.add(a+"."+".")
            ans.add(a+"."+c)
            ans.add("."+b+c)
            ans.add("."+b+".")
            ans.add("."+"."+c)
# print(ans)
print(len(ans))
