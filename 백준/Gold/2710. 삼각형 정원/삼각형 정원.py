for test in range(int(input())):
    x1, y1, x2, y2, x3, y3 = list(map(float, input().split()))
    p1, p2, p3 = complex(x1,y1), complex(x2,y2), complex(x3,y3)
    mx = (x1+x2)/2
    my = (y1+y2)/2
    a = 3
    b = p1+p2+p3
    c = p1*p2+p1*p3+p2*p3
    z1 = (b+(b*b-a*c) ** 0.5)/3
    z2 = (b-(b*b-a*c) ** 0.5)/3
    x1 = z1.real
    y1 = z1.imag
    x2 = z2.real
    y2 = z2.imag
    pp1 = (x1,y1)
    pp2 = (x2,y2)
    if pp2 < pp1:
        pp1, pp2 = pp2, pp1
    x1,y1 = pp1
    x2,y2 = pp2
    d = ((x1-mx)**2+(y1-my)**2)**0.5 + ((x2-mx)**2+(y2-my)**2)**0.5
    print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(x1,y1,x2,y2,d))