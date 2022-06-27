import sys
input = lambda: sys.stdin.readline().strip()

for test in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    ans = 'A'
    for i in range(n):
        if i%2==0:
            if i < n-1:
                t = ''
                for j in range(arr[i]-1):
                    t+=chr(j+ord('B'))
                t+=chr(max(arr[i+1], arr[i])+ord('A'))
            else:
                t = ''
                for j in range(arr[i]):
                    t += chr(j+ord('B'))
            ans += t
        else:
            t = ''
            for j in range(arr[i]):
                t+=chr(j+ord('A'))
            ans+=t[::-1]
    print(f"Case #{test+1}: {ans}")
