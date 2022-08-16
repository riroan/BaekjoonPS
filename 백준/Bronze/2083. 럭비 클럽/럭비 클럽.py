while 1:
    a,b,c=input().split()
    if a == '#':
        break
    b=int(b)
    c=int(c)
    if b > 17 or c>=80:
        print(a, "Senior")
    else:
        print(a, "Junior")