import sys
from random import getrandbits

RANDOM = getrandbits(64)
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"Case #{test+1}: ",end="")
    if arr[2]>=arr[0]+arr[1]:
        print("invalid!")
    elif arr[0] ==arr[1]==arr[2]:
        print("equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2] or arr[2] == arr[0]:
        print("isosceles")
    else:
        print("scalene")