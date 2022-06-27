try:
    d = 0
    start = 0
    speed = 0
    while True:
        s = input().split()
        if len(s) == 2:
            a, b = s
            h, m, s = map(int, a.split(":"))
            
            t = h*3600+m*60+s
            d += speed*(t-start)
            start = t
            speed = int(b)/3600
        else:
            a = s[0]
            h, m, s = map(int, a.split(":"))
            t = h*3600+m*60+s
            print(a,end = " ")
            print("{:.2f} km".format(speed * (t-start)+d))

except:
    pass
