#https://yukicoder.me/problems/no/419

t = list(map(int,input().split()))

if t[0] == t[1]:
    print((2*t[0]**2)**0.5)
else:
    ans = max(t)**2-min(t)**2
    print(ans**0.5)
