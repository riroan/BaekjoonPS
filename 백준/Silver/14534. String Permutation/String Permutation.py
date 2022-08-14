from itertools import permutations
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = list(input())
    print(f"Case # {test+1}:")
    for i in permutations(s):
        print(''.join(i))