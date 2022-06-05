from collections import defaultdict
d = defaultdict(int)
arr = []
try:
    while True:
        arr += input().split()
except:
    pass
for i in arr:
    d[i]+=1
for i in ["Re","Pt","Cc","Ea","Tb","Cm","Ex"]:
    print(i, d[i], "{:.2f}".format(d[i]/len(arr)))
print("Total", len(arr), "1.00")