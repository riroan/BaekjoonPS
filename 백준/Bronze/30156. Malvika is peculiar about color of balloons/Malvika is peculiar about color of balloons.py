# author:  riroan
# created:  2024.02.02 20:38:34
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    s = input()
    print(min(s.count('a'), s.count('b')))
