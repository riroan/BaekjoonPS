from math import *
n,m = map(int, input().split())
[input() for i in range(n)]
d = {i:0 for i in "RGB"}
for i in range(m):d[input().split()[2]]+=1
a=ceil(d["G"]/2)+d["R"]
b=d["G"]//2 + d["B"]
if a > b:
    print("jhnah917")
else:
    print("jhnan917")