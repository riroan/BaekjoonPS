while True:
    a,b=map(int, input().split())
    if a+b == 0:
        break
    if a>b:
        a,b=b,a
    print(2*a-b)