# https://atcoder.jp/contests/past202004-open/tasks/past202004_j

S = input()
change_flag = True
while change_flag:
    stack = []
    change_flag = False
    for i,s in enumerate(S):
        if s == '(':
            stack.append(i)
        elif s == ')':
            l = stack.pop()+1
            r = i
            # ()を取り除くごとにSを作り直している
            S = S[:l-1]+S[l:r]+S[l:r][::-1]+S[r+1:]
            change_flag = True
            break
print(S)