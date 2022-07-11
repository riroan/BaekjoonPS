a,p=map(int, input().split())
s = set()
s.add(a)
def f(x):
    arr = list(map(int, list(str(x))))
    ret = 0
    for i in arr:
        ret += i**p
    return ret
brr = [a]
while True:
    a = f(a)
    if a in s:
        for i in range(len(brr)):
            if brr[i] == a:
                print(i)
                break
        break
    s.add(a)
    brr.append(a)