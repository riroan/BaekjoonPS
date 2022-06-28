import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    ans = ''
    n = int(input())
    for i in range(n):
        t = input()
        for j in range(10):
            s=t.replace('x',str(j))
            a,b = s.split()
            if a[0] == '0' or b[0] == '0':
                continue
            a,b=map(int, [a,b])
            try:
                if a%b == 0:
                    ans+=str(j)
                    break
            except:
                continue
    print(ans)