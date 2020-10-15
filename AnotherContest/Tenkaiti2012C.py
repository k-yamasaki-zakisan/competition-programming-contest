#https://atcoder.jp/contests/tenka1-2012-qualC/tasks/tenka1_2012_10

mark = ["S","H","D","C"]
number = ["A","2","3","4","5","6","7","8","9","1","J","Q","K"]
ok = ["A","1","J","Q","K"]
memo = {"S":set([]),"H":set([]),"D":set([]),"C":set([])}

S = list(input())
tmp = ''
card = []
for i in range(len(S)):
    s = S[i]
    if s == '0':
        continue
    if s in mark:
        tmp = s
    elif s in number:
        if s == '1':
            s = '10'
        tmp += s
        card.append(tmp)
    i += 1

for c in card:
    if c[1] in ok:
        if c[0] in memo:
            memo[c[0]].add(c[1])
    if len(memo[c[0]]) == 5:
        ans_c = c[0]
        ans_stop = c
        break

ans = ''
for c in card:
    if c[0] != ans_c or c[1] not in ok:
        ans += c
    if c == ans_stop:
        break
if ans:
    print(ans)
else:
    print(0)