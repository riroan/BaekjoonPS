# author:  riroan
# created:  2023.10.19 22:22:58
import sys
def input(): return sys.stdin.readline().strip()


arr = input().split()
brr = []
for i in arr:
    if i not in ["bubble", "tapioka"]:
        brr.append(i)
if brr:
    print(*brr)
else:
    print("nothing")
