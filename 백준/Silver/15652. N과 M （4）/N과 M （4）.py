s = input().split(' ')
a, b = int(s[0]), int(s[1])

def f(x, y):
    if len(y)>=2:
        if y[len(y)-2] >y[len(y)-1]:
            return
    if len(y) == b:
        y = [str(i) for i in y]
        print(' '.join(y))
        return
    for i in range(len(x)):
        f(x,y+[x[i]])

d = [i for i in range(1,a+1)]

f(d,[])