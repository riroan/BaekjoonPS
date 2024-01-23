# author:  riroan
# created:  2024.01.23 20:59:08
import sys
input = lambda: sys.stdin.readline().strip()

n,m,k = map(int, input().split())

cnt = 0
while 1:
    cnt +=1
    if k * cnt >= m*cnt+n:
        print(cnt)
        break
