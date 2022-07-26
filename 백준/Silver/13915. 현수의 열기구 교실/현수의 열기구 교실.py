try:
    while 1:
        n=int(input())
        arr = set()
        for i in range(n):
            s = list(map(int, list(input())))
            s = list(set(s))
            s.sort()
            arr.add(tuple(s))
        print(len(arr))
except:
    pass