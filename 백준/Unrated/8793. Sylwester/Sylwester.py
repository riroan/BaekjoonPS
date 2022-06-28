import sys
def input(): return sys.stdin.readline().strip()


for test in range(int(input())):
    ans = 0
    n = int(input())
    s = 0
    arr = [int(input()) for i in range(n)]
    for i in arr:
        s+=i
        if s<0:
            ans+=1
            s+=1
    print(s+ans)
