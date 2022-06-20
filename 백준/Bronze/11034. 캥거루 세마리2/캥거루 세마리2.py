try:
    while True:
        a,b,c=map(int, input().split())
        d1 = b-a
        d2 = c-b
        print(max(d1,d2)-1)
except:
    pass