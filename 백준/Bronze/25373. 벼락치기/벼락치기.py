n = int(input())
l = 0
r = 10**18
while l + 1 < r:
    x = (l+r)//2
    s = 0
    for i in range(7):
        if x-i>0:
            s += x-i
    if s < n:
        l = x
    else:
        r = x
print(r)