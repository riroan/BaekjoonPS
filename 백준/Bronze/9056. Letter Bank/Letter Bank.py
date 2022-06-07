import sys
input = sys.stdin.readline

for test in range(int(input())):
    a, b = input().strip().split()
    d = {}
    for i in a:
        d[i] = 0
    ok = True
    for i in b:
        try:
            d[i]+=1
        except:
            ok = False
    for i in d:
        if d[i]==0:
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")