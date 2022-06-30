x = input()
y = input()
z = input()
k = int(input())


def f(x):
    s = set()
    for i in range(2**len(x)):
        t = ''
        for j in range(len(x)):
            if i & (1 << j):
                t += x[j]
            if len(t) == k:
                s.add(t)
    return s


xx = f(x)
yy = f(y)
zz = f(z)
ans = set()
for i in xx:
    if i in yy or i in zz:
        ans.add(i)
for i in yy:
    if i in zz:
        ans.add(i)
ans = list(ans)
ans.sort()
if ans:
    for i in ans:
        print(i)
else:
    print(-1)