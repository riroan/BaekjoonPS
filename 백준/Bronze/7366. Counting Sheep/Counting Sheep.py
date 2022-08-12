import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    n = int(input())
    arr = input().split()
    print(f"Case {test+1}: This list contains {arr.count('sheep')} sheep.\n")
