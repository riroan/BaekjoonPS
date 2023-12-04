a,b = input().split()
a = int(a)
if b == 'miss':
    print(0)
elif b == 'bad':
    print(a*200)
elif b == 'cool':
    print(a * 400)
elif b == 'great':
    print(a*600)
else:
    print(1000*a)