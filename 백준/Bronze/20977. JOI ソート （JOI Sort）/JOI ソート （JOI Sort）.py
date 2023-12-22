# author:  riroan
# created:  2023.12.22 21:45:33
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(input())
d = {"J":0, "O":1, "I":2}
arr = [[d[arr[i]], arr[i]] for i in range(n)]
arr.sort()
for i,j in arr:
    print(j, end="")
