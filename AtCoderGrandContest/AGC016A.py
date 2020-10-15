S = list(input())
S += '$'
Alph = [chr(ord('a') + i) for i in range(26)]

ans = len(S)
#アルファベット全てを探索(引っかかるまでの個数の最小値が答え)
for alth in Alph:
    tmp = 0
    tmp_ans = 0
    for i in range(len(S)):
        if i == len(S)-1:
            tmp_ans = max(tmp_ans, tmp)
        elif S[i] == alth:
            tmp_ans = max(tmp_ans, tmp)
            tmp = 0
        else:
            tmp += 1
    ans = min(ans, tmp_ans)
print(ans)