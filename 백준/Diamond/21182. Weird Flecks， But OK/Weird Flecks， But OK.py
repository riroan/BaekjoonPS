import random
import sys
input = lambda: sys.stdin.readline().strip()

eps = 1e-9


class Circle:
    def __init__(self, p, r):
        self.p = p
        self.r = r


def dist(a, b):
    return abs(a - b)


def area2(p, q):
    return (p.conjugate() * q).imag


def isIn(c, p):
    return dist(c.p, p) < c.r + eps


INVAL = Circle(complex(0, 0), -1)


def norm(a):
    return a.real ** 2 + a.imag ** 2


def mCC(a, b, c):
    b -= a
    c -= a
    d = 2 * (b.conjugate() * c).imag
    if abs(d) < eps:
        return INVAL
    ans = complex(c * norm(b) - b * norm(c)) * complex(0, -1) / d
    return Circle(a + ans, abs(ans))


def solve(p):
    random.shuffle(p)
    c = INVAL
    for i in range(len(p)):
        if c.r < 0 or not isIn(c, p[i]):
            c = Circle(p[i], 0)
            for j in range(i + 1):
                if not isIn(c, p[j]):
                    ans = Circle((p[i] + p[j]) * 0.5, dist(p[i], p[j]) * 0.5)
                    if c.r == 0:
                        c = ans
                        continue
                    l = INVAL
                    r = INVAL
                    pq = p[j] - p[i]
                    for k in range(j + 1):
                        if not isIn(ans, p[k]):
                            a2 = area2(pq, p[k] - p[i])
                            c = mCC(p[i], p[j], p[k])
                            if c.r < 0:
                                continue
                            elif a2 > 0 and (l.r < 0 or area2(pq, c.p - p[i]) > area2(pq, l.p - p[i])):
                                l = c
                            elif a2 < 0 and (r.r < 0 or area2(pq, c.p - p[i]) < area2(pq, r.p - p[i])):
                                r = c
                    if l.r < 0 and r.r < 0:
                        c = ans
                    elif l.r < 0:
                        c = r
                    elif r.r < 0:
                        c = l
                    else:
                        if l.r <= r.r:
                            c = l
                        else:
                            c = r
    return c

def f(xx,yy):
    arr = []
    for x,y in zip(xx,yy):
        arr.append(complex(x,y))
    answer = solve(arr)
    return answer

n = int(input())
arr = []
x,y,z = [],[],[]
for _ in range(n):
    a,b,c = map(float, input().split())
    x.append(a)
    y.append(b)
    z.append(c)
ans1, ans2, ans3 = f(x,y),f(y,z),f(x,z)
print(min(ans1.r,ans2.r,ans3.r)*2)