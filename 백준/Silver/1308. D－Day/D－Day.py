from datetime import datetime
y1,m1,d1 = map(int, input().split())
y2,m2,d2 = map(int, input().split())
dd = (datetime(y2, m2, d2)-datetime(y1, m1, d1)).days
if y2>1000 + y1 or y2==y1+1000 and m1<=m2 and d1<=d2:
    print("gg")
else:
    print(f"D-{dd}")