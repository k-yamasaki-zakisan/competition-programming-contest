# https://atcoder.jp/contests/typical90/tasks/typical90_r

from math import sin, cos, radians, degrees, atan2

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]
for e in E:
    y = -L/2*sin(radians(360*e/T))
    z = L/2-L/2*cos(radians(360*e/T))
    b = (abs(y-Y)**2+X**2)**0.5
    print(degrees(atan2(z, b)))
