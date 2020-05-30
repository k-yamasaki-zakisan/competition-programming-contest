#https://atcoder.jp/contests/arc010/tasks/arc010_2

calender = [0]*367
 
memo = {1:0, 2:31, 3:60, 4:91, 5:121,
        6:152, 7:182, 8:213, 9:244, 10:274, 11:305, 12:335}
 
for i in range(367):
    if i%7==1 or i%7==0:
        calender[i] = 1
        
calender[0] = 0
 
n=int(input())
for i in range(n):
    s=list(input())
    month = s[0]
    for j in range(1,len(s)):
        if s[j] =='/':
            month = int(''.join(map(str,month)))
            day = int(''.join(map(str,s[j+1:])))
            break
        else:
            month = month+s[j]
    if calender[memo[month]+day] == 0:
        calender[memo[month]+day] = 1
    else:
        next_holiday=memo[month]+day
        while calender[next_holiday] == 1 and next_holiday < 366:
            next_holiday += 1
        calender[next_holiday] = 1
#print(calender)
count = 0
ans = 0
for i in range(367):
    if calender[i] == 1:
        count += 1
    else:
        ans = max(count,ans)
        count = 0
ans = max(count,ans)
print(ans)
