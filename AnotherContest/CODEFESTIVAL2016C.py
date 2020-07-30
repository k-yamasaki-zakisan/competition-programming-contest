#https://atcoder.jp/contests/code-festival-2016-quala/tasks/codefestival_2016_qualA_c

s=list(input())

k=int(input())

ans = []

for alf in s:
    if alf == 'a':
        ans.append('a')
    else:
        if 123 - ord(alf) <= k:
            k -= 123 - ord(alf)
            ans.append('a')
        else:
            ans.append(alf)
if 0 < k:
    amari = (ord(ans[-1])-97+k)%26
    ans[-1] = chr(amari+97)
    
print(''.join(map(str,ans)))
