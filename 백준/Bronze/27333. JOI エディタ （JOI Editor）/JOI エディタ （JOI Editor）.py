# author:  riroan
# created:  2024.01.04 08:01:12
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
s = input().replace("jj", "JJ").replace("oo", "OO").replace("ii", "II")
print(s)

