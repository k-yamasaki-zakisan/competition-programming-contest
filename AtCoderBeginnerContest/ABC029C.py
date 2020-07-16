#https://atcoder.jp/contests/abc029/tasks/abc029_c

n=int(input())
 
ans = ['a','b','c']
 
while len(ans)>0:
    moji = ans.pop(0)
    if len(list(moji)) < n:
        ans.append(moji+'a')
        ans.append(moji+'b')
        ans.append(moji+'c')
    else:
        print(moji)
