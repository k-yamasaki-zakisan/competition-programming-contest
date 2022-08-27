Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())


def vec(a, b):
    return (a[0] - b[0], a[1] - b[1])


def tri_in(a, b, c, p):
    ab = vec(b, a)
    bp = vec(p, b)

    bc = vec(c, b)
    cp = vec(p, c)

    ca = vec(a, c)
    ap = vec(p, a)

    c1 = ab[0] * bp[1] - ab[1] * bp[0]
    c2 = bc[0] * cp[1] - bc[1] * cp[0]
    c3 = ca[0] * ap[1] - ca[1] * ap[0]

    return (0 < c1 and 0 < c2 and 0 < c3) or (0 > c1 and 0 > c2 and 0 > c3)


for a, b, c, d in [
    [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)],
    [(Ax, Ay), (Bx, By), (Dx, Dy), (Cx, Cy)],
    [(Ax, Ay), (Cx, Cy), (Dx, Dy), (Bx, By)],
    [(Dx, Dy), (Bx, By), (Cx, Cy), (Ax, Ay)],
]:
    if tri_in(a, b, c, d):
        print("No")
        exit()
print("Yes")
