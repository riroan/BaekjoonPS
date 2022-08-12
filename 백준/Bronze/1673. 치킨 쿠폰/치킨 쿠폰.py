try:
    while 1:
        a, b = map(int, input().split())
        ans = 0
        c, s = a, 0
        while c:
            ans += c
            s += c
            c = s//b
            s -= s//b*b
        print(ans)
except:
    pass
