# author:  riroan
# created:  2023.10.28 20:43:38
import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    print('01'[int(input())%10==0])
