# author:  riroan
# created:  2024.02.17 22:14:52
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))
k = n+1 >> 1
s = arr.count(1)
print(max(0, k-s))
