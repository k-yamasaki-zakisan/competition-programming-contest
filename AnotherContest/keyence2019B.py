#https://atcoder.jp/contests/keyence2019/tasks/keyence2019_b

S = input()

for i in range(len(S)-1):
    for j in range(i,len(S)):
        memo = S[:i]+S[j:]
        #print(memo)
        if memo == 'keyence':
            print('YES')
            exit()
print('NO')
