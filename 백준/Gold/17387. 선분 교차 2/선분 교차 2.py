a, b, c, d = map(int, input().split())
x, y, z, w = map(int, input().split())
A = (a, b)
B = (c, d)
C = (x, y)
D = (z, w)


def big(a, b):
    if a[0] > b[0]:
        return True
    elif a[0] == b[0]:
        return a[1] > b[1]
    return False


def ccw(p1, p2, p3):
    f1 = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
    f2 = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
    op = f1 - f2
    if op > 0:
        return 1
    elif op == 0:
        return 0
    else:
        return -1


ab = ccw(A, B, C) * ccw(A, B, D)
cd = ccw(C, D, A) * ccw(C, D, B)

if ab == 0 and cd == 0:
    if big(A, B):
        A, B = B, A
    if big(C, D):
        C, D = D, C
    f = not (big(C, B) or big(A, D))
    if f:
        print(1)
    else:
        print(0)
elif ab <= 0 and cd <= 0:
    print(1)
else:
    print(0)
