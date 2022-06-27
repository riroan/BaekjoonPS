import string
import math
arr = []
try:
    while True:
        arr+=input().split()
except:
    sss = set(string.ascii_letters)
    arr = [i.lower() for i in arr]
    cnt = 0
    s = set()
    ss = 0
    for i in arr:
        if i == 'bullshit':
            ss += len(s)
            s = set()
            cnt+=1
        else:
            t = ''
            for j in i:
                if j in sss:
                    t+=j
                else:
                    if t:
                        s.add(t)
                        t = ''
            if t:
                s.add(t)
    g = math.gcd(ss, cnt)
    ss//=g
    cnt//=g
    print(f'{ss} / {cnt}')