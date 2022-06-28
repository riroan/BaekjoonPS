import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n = int(input())
    x,y = 0,0
    for i in input():
        if i == 'N':
            x+=1
        if i == 'S':
            x-=1
        if i == 'E':
            y+=1
        if i == 'W':
            y-=1
    print(abs(x)+abs(y))