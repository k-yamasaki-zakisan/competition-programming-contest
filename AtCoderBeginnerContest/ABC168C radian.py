#https://atcoder.jp/contests/abc168/tasks/abc168_c

import math

a,b,h,m = map(int,input().split())

minitu = 360*(m/60)

hour = 360*(h/12)+(360//12)*(m/60)

kakudo = min(abs(hour-minitu),360-abs(hour-minitu))

kakudo_ra = math.radians(kakudo)

c = (a**2+b**2-2*a*b*math.cos(kakudo_ra))**0.5

print(c)
