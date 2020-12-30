# https://atcoder.jp/contests/past202012-open/tasks/past202012_a

S = input()
for i in range(len(S)-2):
    if S[i:i+3] == 'ooo':
        print('o')
        exit()
    elif S[i:i+3] == 'xxx':
        print('x')
        exit()
print('draw')
