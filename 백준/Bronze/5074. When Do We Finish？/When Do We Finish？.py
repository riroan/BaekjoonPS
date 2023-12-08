# author:  riroan
# created:  2023.12.08 11:01:09
import sys
input = lambda: sys.stdin.readline().strip()

while 1:
    a,b = input().split()
    aa,bb = map(int, a.split(":"))
    cc,dd = map(int, b.split(":"))
    if aa==bb==cc==dd==0:
        break
    x = aa*60+bb
    y = cc*60+dd
    ok = 0
    z = y + x
    if z >= 24*60:
        ok = z // (24*60)
        z-=24*60 * ok
    x = str(z//60)
    y=str(z%60)
    if len(x) == 1:
        x = '0' + x
    if len(y) == 1:
        y = '0'+y

    print(f"{x}:{y}",end="")
    if ok:
        print(f" +{ok}")
    else:
        print()

