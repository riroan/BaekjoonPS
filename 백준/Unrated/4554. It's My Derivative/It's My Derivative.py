import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    print("POLYNOMIAL", test+1)
    xx, s = input().split()
    print(s)
    xx = int(xx)
    arr = []
    last = 0
    i = 0
    while i < len(s):
        if s[i] == 'x':
            ix = i
            t = ''
            while ix:
                ix -= 1
                t = s[ix] + t
                if (s[ix] == '+' or s[ix] == '-'):
                    break
            if t == '+':
                t = '1'
            if t == '-':
                t = '-1'
            if t == '':
                t = 1
            else:
                try:
                    t = int(t)
                except:
                    t = int(t[1:])
            u = ''
            ix = i

            if ix == len(s) - 1:
                u = '1'
            else:
                if s[ix+1] == '^':
                    ix += 1
                    while ix < len(s)-1:
                        ix += 1
                        if s[ix] == '+' or s[ix] == '-':
                            break
                        u += s[ix]
                else:
                    u = '1'
            last = ix
            if u == '':
                u = '1'
            arr.append([t, int(u)])
        i += 1
    if not arr:
        print(0)
        print(0)
        print(0)
        print(0)
        continue
    ss = ''
    x, y = arr[0]
    ss += str(x*y)
    if y > 2:
        ss += 'x^'+str(y-1)
    elif y == 2:
        ss += 'x'
    brr = [[x*y, y-1]]
    for x, y in arr[1:]:
        if y == 0:
            continue
        t = x*y
        if t > 0:
            ss += '+'
        ss += str(t)
        if y > 2:
            ss += 'x^'+str(y-1)
        elif y == 2:
            ss += 'x'
        brr.append([x*y, y-1])
    print(ss)
    print(ss.replace("x", f"({str(xx)})"))
    crr = []
    for x, y in brr:
        crr.append(x*pow(xx, y))
    sss = ''
    for i in crr:
        if i < 0:
            sss += str(i)
        else:
            sss += '+'+str(i)
    if sss[0] == '+':
        sss = sss[1:]
    print(sss)
    print(eval(sss))
