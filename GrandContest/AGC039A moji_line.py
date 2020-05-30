#https://atcoder.jp/contests/agc039/tasks/agc039_a

S=input()
K=int(input())
 
if list(S).count(S[0])==len(S):
    print(len(S)*K//2)
 
else:
    S_count=0
    i=0
    while i<len(S)-1:
        if S[i]==S[i+1]:
            S_count+=1
            i+=1
        i+=1
 
    if S[0]==S[-1]:
        a=1
        i=0
        while i<len(S)-1:
            if S[i]==S[i+1]:
                a+=1
                i+=1
            else:
                break
        b=1
        i=len(S)-1
        while i>0:
            if S[i]==S[i-1]:
                b+=1
                i+=-1
            else:
                break
 
        S_count*=K
        S_count-=(K-1)*(a//2 + b//2 - (a+b)//2)
 
    else:
        S_count*=K
    print(S_count)
